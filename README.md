# 学生管理アプリ：システムアーキテクチャ

佐藤マナブさんの「課題・出席・成績の一元管理」を実現するための、クライアントからデータベースまでの全体構成です。

## 1. システムダイアグラム (System Diagram)

```mermaid
graph LR
    subgraph "User Interface (Client)"
        User((学生/マナブ)) --> MobileApp[モバイルアプリ/Web]
        MobileApp --> |授業・課題確認| Dashboard[ダッシュボードUI]
        MobileApp --> |出席ボタン| AttendanceUI[出席記録UI]
    end

    subgraph "Application Logic (Backend)"
        Dashboard --> |APIリクエスト| AuthFunc[認証・認可機能]
        AttendanceUI --> |位置情報/タップ| AttenFunc[出席判定機能]
        
        subgraph "Core Functions"
            AuthFunc --> CardRec[課題・スケジュール管理]
            AttenFunc --> Animation[通知・進捗表示処理]
            Judgment[成績目安判定ロジック]
        end
    end

    subgraph "Data Storage & External"
        CardRec <--> DB[(メインデータベース)]
        Animation --> PushServer[通知サーバー]
        DB --- LogStore[(学習・出席ログ)]
        
        Internet((インターネット)) --- UnivSystem[大学LMS/外部API]
        UnivSystem --> DB
    end

    %% スタイル定義
    style MobileApp fill:#f9f,stroke:#333,stroke-width:2px
    style DB fill:#00f,stroke:#fff,stroke-width:2px,color:#fff
    style UnivSystem fill:#fff,stroke:#333,stroke-dasharray: 5 5
