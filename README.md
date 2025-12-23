<mxfile host="app.diagrams.net" modified="2025-12-23T01:00:00Z" agent="Mozilla/5.0" version="24.7.0" editor="draw.io">
  <diagram id="student-app-architecture" name="System Architecture">
    <mxGraphModel dx="1134" dy="754" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- 学生スマホアプリ -->
        <mxCell id="studentApp" value="学生スマホアプリ&#10;（授業・課題・出席管理）" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="60" y="160" width="200" height="80" as="geometry"/>
        </mxCell>

        <!-- 大学側管理画面 -->
        <mxCell id="adminWeb" value="大学側Web管理画面&#10;（教員・職員用ダッシュボード）" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="60" y="280" width="200" height="80" as="geometry"/>
        </mxCell>

        <!-- インターネット/ネットワーク -->
        <mxCell id="internet" value="インターネット / ネットワーク" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;dashed=1;" vertex="1" parent="1">
          <mxGeometry x="300" y="210" width="200" height="80" as="geometry"/>
        </mxCell>

        <!-- ロードバランサ / API Gateway -->
        <mxCell id="apiGateway" value="ロードバランサ / API Gateway" style="shape=process;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="540" y="210" width="200" height="80" as="geometry"/>
        </mxCell>

        <!-- アプリケーションサーバ -->
        <mxCell id="appServer" value="アプリケーションサーバ&#10;（REST API）" style="swimlane;childLayout=stackLayout;horizontal=1;startSize=26;rounded=1;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="800" y="140" width="220" height="160" as="geometry"/>
        </mxCell>

        <mxCell id="appServerNode1" value="APIサーバ #1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#82b366;" vertex="1" parent="appServer">
          <mxGeometry x="10" y="40" width="200" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="appServerNode2" value="APIサーバ #2" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#82b366;" vertex="1" parent="appServer">
          <mxGeometry x="10" y="90" width="200" height="40" as="geometry"/>
        </mxCell>

        <!-- 通知サービス -->
        <mxCell id="notificationService" value="通知サービス&#10;（プッシュ通知 / メール）" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="800" y="330" width="220" height="80" as="geometry"/>
        </mxCell>

        <!-- データベース -->
        <mxCell id="database" value="RDBMS&#10;（PostgreSQL / MySQL）" style="shape=cylinder;whiteSpace=wrap;html=1;boundedLbl=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="1080" y="180" width="140" height="120" as="geometry"/>
        </mxCell>

        <!-- キャッシュ（任意） -->
        <mxCell id="cache" value="キャッシュ&#10;（Redis 等 / 任意）" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e2f0d9;strokeColor=#70ad47;dashed=1;" vertex="1" parent="1">
          <mxGeometry x="1080" y="60" width="160" height="80" as="geometry"/>
        </mxCell>

        <!-- 学生アプリ → インターネット -->
        <mxCell id="edge1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;" edge="1" parent="1" source="studentApp" target="internet">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- 管理画面 → インターネット -->
        <mxCell id="edge2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;" edge="1" parent="1" source="adminWeb" target="internet">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- インターネット → API Gateway -->
        <mxCell id="edge3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;" edge="1" parent="1" source="internet" target="apiGateway">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- API Gateway → アプリケーションサーバ -->
        <mxCell id="edge4" value="HTTPS / REST API" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;fontSize=10;" edge="1" parent="1" source="apiGateway" target="appServer">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- アプリケーションサーバ → DB -->
        <mxCell id="edge5" value="SQL" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;fontSize=10;" edge="1" parent="1" source="appServer" target="database">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- アプリケーションサーバ → 通知サービス -->
        <mxCell id="edge6" value="通知ジョブ / キュー" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;fontSize=10;" edge="1" parent="1" source="appServer" target="notificationService">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- 通知サービス → 学生スマホ（プッシュ） -->
        <mxCell id="edge7" value="プッシュ通知（FCM等）" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;endArrow=block;endFill=1;fontSize=10;" edge="1" parent="1" source="notificationService" target="studentApp">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- アプリケーションサーバ → キャッシュ -->
        <mxCell id="edge8" value="キャッシュ参照 / 更新" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;endArrow=block;endFill=1;fontSize=10;" edge="1" parent="1" source="appServer" target="cache">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile># -
