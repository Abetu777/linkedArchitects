import re
import requests


def get_architects_list():
    url = "https://ja.wikipedia.org/w/api.php"

    # ページのタイトルを指定
    params = {
        "action": "parse",
        "page": "日本の建築家一覧",
        "format": "json",
        "prop": "wikitext"
    }

    response = requests.get(url, params=params)
    content = response.json()
    if 'error' in content:
        print("エラーが発生しました:", content['error']['info'])
        return None
    else:
        return content

content = get_architects_list()

content_text = content['parse']['wikitext']['*']

matches = re.findall(r'\[\[(.*?)\]\]', content_text)

archList = []
# 抽出された文字列を出力
for match in matches:
    archList.append(match)

print(len(archList))
