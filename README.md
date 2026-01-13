graph TD
    subgraph "スマホ (学生用)"
        App[シンプル管理画面]
    end

    subgraph "クラウド (Backend as a Service)"
        DB[(データ保存箱)]
        Logic{自動判定}
    end

    %% 流れ
    App -->|1. 課題チェック| DB
    App -->|2. 出席ボタン| Logic
    Logic -->|3. 結果保存| DB
    DB -->|4. あと○日と通知| App
