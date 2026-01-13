### システム構成図

```mermaid
graph TD
    User((学生)) -->|操作| App[スマホアプリ]
    App -->|データ保存| DB[(データベース)]
    DB -->|通知| App
