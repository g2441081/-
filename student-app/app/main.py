from flask import Flask, render_template, request, redirect
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

# Flaskアプリの初期化
app = Flask(__name__)

# データベース(PostgreSQL)の設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- データベースのテーブル定義 ---
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)        # 識別用ID
    course = db.Column(db.String(100), nullable=False)   # 授業名
    title = db.Column(db.String(100), nullable=True)     # 課題名（空でもOK）
    deadline = db.Column(db.String(50), nullable=True)   # 締切日時（空でもOK）
    attendance = db.Column(db.Integer, default=0)       # 出席回数（初期値0）

# 起動時にテーブルを自動作成
with app.app_context():
    db.create_all()

# --- ルーティング（各画面・機能の処理） ---

# 1. メイン画面の表示
@app.route('/')
def index():
    try:
        # すべてのデータを授業名順に取得
        tasks = Task.query.order_by(Task.course).all()
        
        # 現在時刻と「期限直前」とみなす基準（明日いっぱい）を計算
        now = datetime.now()
        current_time_str = now.strftime('%Y-%m-%dT%H:%M')
        tomorrow_end = (now + timedelta(days=1)).replace(hour=23, minute=59, second=59)
        notification_limit = tomorrow_end.strftime('%Y-%m-%dT%H:%M')
        
        # カレンダー表示用のデータ作成
        calendar_events = []
        for t in tasks:
            # 課題名と締切があるものだけカレンダーに載せる
            if t.title and t.deadline:
                # 締切状況に応じて色を決定
                if t.deadline < current_time_str:
                    event_color = "#6c757d" # 終了：グレー
                elif t.deadline <= notification_limit:
                    event_color = "#ff4757" # 直前：赤
                else:
                    event_color = "#007bff" # 通常：青
                
                calendar_events.append({
                    "title": f"{t.course}: {t.title}",
                    "start": t.deadline,
                    "backgroundColor": event_color,
                    "borderColor": event_color,
                    "allDay": False
                })

        # HTMLテンプレートにデータを渡して表示
        return render_template('index.html', 
                               tasks=tasks, 
                               current_time_str=current_time_str,
                               notification_limit=notification_limit,
                               calendar_events=json.dumps(calendar_events))
    except Exception as e:
        return f"エラーが発生しました: {e}", 500

# 2. 新規データの追加
@app.route('/add', methods=['POST'])
def add():
    course = request.form.get('course')
    title = request.form.get('title')
    deadline = request.form.get('deadline')

    # 同じ授業の既存データがあれば、現在の出席回数を引き継ぐ
    existing_task = Task.query.filter_by(course=course).first()
    current_attendance = existing_task.attendance if existing_task else 0

    # 課題を追加する場合、授業名だけの「空データ」があれば削除して整理
    if title:
        empty_task = Task.query.filter_by(course=course, title=None).first()
        if empty_task:
            db.session.delete(empty_task)
            db.session.commit()

    # 新しいデータを保存
    new_task = Task(course=course, 
                    title=title if title else None, 
                    deadline=deadline if deadline and deadline.strip() else None, 
                    attendance=current_attendance)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

# 3. 出席回数を増やす
@app.route('/attend/<int:id>', methods=['POST'])
def attend(id):
    task = Task.query.get(id)
    if task:
        # 同じ授業名のデータすべての出席カウントを+1する（同期処理）
        for t in Task.query.filter_by(course=task.course).all():
            t.attendance += 1
        db.session.commit()
    return redirect('/')

# 4. 出席回数を減らす
@app.route('/unattend/<int:id>', methods=['POST'])
def unattend(id):
    task = Task.query.get(id)
    if task and task.attendance > 0:
        # 同じ授業名のデータすべての出席カウントを-1する
        for t in Task.query.filter_by(course=task.course).all():
            t.attendance -= 1
        db.session.commit()
    return redirect('/')

# 5. 課題の完了・授業の削除
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    task = Task.query.get(id)
    if task:
        course_name, current_attendance = task.course, task.attendance
        db.session.delete(task)
        db.session.commit()

        # 課題を消した結果、その授業のデータがゼロになった場合
        # 授業名と出席回数だけを保持した空データを作成する（授業情報を残すため）
        remaining_tasks = Task.query.filter_by(course=course_name).count()
        if remaining_tasks == 0 and request.form.get('keep_course') != 'false':
            db.session.add(Task(course=course_name, title=None, deadline=None, attendance=current_attendance))
            db.session.commit()
    return redirect('/')

# サーバーの起動設定
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)