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
    data = response.json()
    if 'error' in data:
        print("エラーが発生しました:", data['error']['info'])
        return None
    else:
        return data

content = get_architects_list()

# 取得したデータの構造を確認
# print(content)  # データの構造を確認するための出力

# 必要な情報を適切に抽出
content_text = content['parse']['wikitext']['*']


# 抽出した情報をファイルに書き込む
with open('archiContext.txt', 'w', encoding='utf-8') as f:
    f.write(content_text)

matches = re.findall(r'\[\[(.*?)\]\]', content_text)
archList = []
# 抽出された文字列を出力
for match in matches:
    archList.append(match)
