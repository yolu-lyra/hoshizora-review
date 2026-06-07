import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "zodiac.json"

with open(DATA_FILE, "r" , encoding="utf-8") as f:
    zodiac_list = json.load(f)

html = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>星空案内人復習サイト</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<h1>黄道十二星座</h1>
"""

for zodiac in zodiac_list:
    html += f"""
    <div class="card">
        <h2>{zodiac["name"]}</h2>
        <p>一等星: {zodiac["bright_star"]}</p>
        <p>見頃: {zodiac["season"]}</p>
        <p>神話: {zodiac["myth"]}</p>
        <details>
            <summary>観測ポイントを見る</summary>
            <p>{zodiac["observation"]}</p>
        </details>
    </div>
    """

html += """
</body>
</html>
"""

OUTPUT_FILE = BASE_DIR / "docs" / "index.html"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print("index.htmlを作成しました。")