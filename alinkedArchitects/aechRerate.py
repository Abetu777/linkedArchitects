import pandas as pd
import requests
import re
from getArchtects import archDf, archList




#一覧のリストからそれぞれのWikipediaのページに行きそのページの中に一覧のリストにある名前があればそれを抽出する

def getRerativArchitects(word: str):
    url = "https://ja.wikipedia.org/w/api.php"

    # ページのタイトルを指定
    params = {
        "action": "parse",
        "page": word,
        "format": "json",
        "prop": "wikitext"
    }

    response = requests.get(url, params=params, timeout=10)

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
        if match not in archList:  # インデックスが列に存在しない場合
            print(f"インデックス '{match}' が列に見つかりませんでした。")
            continue  # 処理を中断して次のループに進む
        else:
            archDf.loc[word][match] += 1