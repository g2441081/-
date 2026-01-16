from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# データベースの設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# データの形（タスク）を決める
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    deadline = db.Column(db.String(50))
    attendance = db.Column(db.Integer, default=0)

# 最初に1回だけデータベースのテーブルを作る
with app.app_context():
    db.create_all()

# メイン画面の表示
@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

# 予定の追加ボタンを押したときの動き
@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    deadline = request.form.get('deadline')
    new_task = Task(title=title, deadline=deadline)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

# 出席ボタンを押したときの動き
@app.route('/attend/<int:id>', methods=['POST'])
def attend(id):
    task = Task.query.get(id)
    task.attendance += 1
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)