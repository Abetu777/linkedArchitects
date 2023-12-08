from pyvis.network import Network
import pandas as pd
import sqlite3

# データベースファイルへの接続
conn = sqlite3.connect('architects.db')
# カーソルを取得
cursor = conn.cursor()
# クエリを実行してデータを取得する例
cursor.execute('SELECT * FROM architects_table')
rows = cursor.fetchall()
# データの取得
# for row in rows:
#     print(row)  # もしくは取得したデータを適切に処理する

# table_name = 'architects_table'
# cursor.execute(f"PRAGMA index_list({table_name})")
indexes_info = cursor.fetchall()

# インデックス情報の取得
for index in indexes_info:
    print(index[1])  # もしくは他の処理に渡す





# net = Network(notebook=True)
# net.add_nodes([1, 2], label=["Alex", "Carthy"])

# df = arch


# net.show('aa.html')