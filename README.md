# Robot
この研究所では精鋭ぞろいのチームによって二足歩行ロボットの開発が行われています。ロボットの各個体は最大 4 方向への移動が可能となっています。しかし 1 歩でどの方向にどれだけ動くかは個体によってまちまちです。

これからロボットの歩行動作の実験を行います。ある個体が正しく動作しているかどうかの確認のためには、一連の命令を与えたのちこの個体が理論上どこに移動しているかを求めるプログラムを作成する必要があります。この研究所のエンジニアであるあなたはこの作成を任されました。


歩行実験は下図のようなコマで区切られた盤上で行います。実験対象の個体の移動領域として個体から見て前方向、右方向、後方向、左方向の順に 1 歩で何コマ動くかが与えられます。

はじめの状態ではロボットは必ず y 座標の正方向 (下図の上方向) を向いています。ロボットが向いている方向が「前方向」となり、そこから時計回りに 90 度ずつ進めた方向がそれぞれ「右方向」、「後方向」、「左方向」となります。

命令は「◯方向に1歩動く」あるいは「◯方向に方向転換する」のいずれかで与えられます。ただし、「前方向に方向転換する」という命令は無意味なので与えられません。


例) 

開始地点: (2, 2) 
移動領域: 2, 1, 1, 1 (前方に 1 歩動く際には 2 コマ、他の方向に 1 歩動く際には 1 コマ動く) 
命令: 
「前方向に 1 歩動く」 → 「右方向に方向転換する」 → 「前方向に 1 歩動く」 → 
「前方向に 1 歩動く」 → 「後方向に方向転換する」 → 「左方向に 1 歩動く」 → 
「左方向に 1 歩動く」 → 「後方向に 1 歩動く」 

→ 到達地点: (7, 2)


入力例1
2 2
2 1 1 1
8
m F
t R
m F
m F
t B
m L
m L
m B

出力例1
7 2
