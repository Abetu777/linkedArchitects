import pandas as pd
from getArchtects import archDf,archList
import requests
import re

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

i=0
for word in archList:
    rerativList = getRerativArchitects(word)
    for match in rerativList:
        if match not in archList:  # インデックスが列に存在しない場合
            print(f"インデックス '{match}' が列に見つかりませんでした。")
            continue  # 処理を中断して次のループに進む
        else:
            i += 1
            pass

            # archDf[word][match] += 1