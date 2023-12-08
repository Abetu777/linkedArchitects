import pandas as pd
from getArchtects import archList
import requests
import re

archList = archList[0:21]

# 行と列にそれぞれarchListの入った空のDataFrameを作成
archDf = pd.DataFrame(index=archList, columns=archList)
archDf = archDf.fillna(0)
# print(archDf)


#archListから一つづつその人のぺーじにいく。そのページの中からリンクがあるものを抽出する。そこからarchListに入っている単語を選ぶ。その要素に＋１する。

# def getRerativArchitects(word:str):
#     url = "https://ja.wikipedia.org/w/api.php"

#     # ページのタイトルを指定
#     params = {
#         "action": "parse",
#         "page": word,
#         "format": "json",
#         "prop": "wikitext"
#     }

#     response = requests.get(url, params=params)
#     data = response.json()
#     content = data['parse']['wikitext']['*']

#     matches = re.findall(r'\[\[(.*?)\]\]', content)
#     rerativList = []
#     # 抽出された文字列を出力
#     for match in matches:
#         if match in archList:
#             rerativList.append(match)

#     if 'error' in data:
#         print("エラーが発生しました:", data['error']['info'])
#         return None
#     else:
#         return rerativList

def getRerativArchitects(word: str):
    url = "https://ja.wikipedia.org/w/api.php"

    # ページのタイトルを指定
    params = {
        "action": "parse",
        "page": word,
        "format": "json",
        "prop": "wikitext"
    }

    response = requests.get(url, params=params)
    data = response.json()

    # 'parse'キーが存在するかどうかをチェックし、存在しない場合は空のリストを返す
    if 'parse' not in data:
        print(f"キー 'parse' が見つかりませんでした。", word)
        return []

    content = data['parse'].get('wikitext', {}).get('*', '')

    matches = re.findall(r'\[\[(.*?)\]\]', content)
    rerativList = []

    for match in matches:
        if match in archList:
            rerativList.append(match)

    return rerativList


for word in archList:
    rerativList = getRerativArchitects(word)
    for match in rerativList:
        archDf.loc[word, match] += 1
    



from sqlalchemy import create_engine

# SQLiteデータベースに接続
engine = create_engine('sqlite:///architects.db')  # データベース名を指定してください

# DataFrameをSQLiteデータベースに書き込む
archDf.to_sql('architects_table', con=engine)