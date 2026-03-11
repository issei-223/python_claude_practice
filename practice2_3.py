import csv
import json
from typing import Dict, List

with open('people.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['鈴木', '26', '東京'])
    writer.writerow(['田中', '16', '札幌'])
    writer.writerow(['菊池', '22', '神戸'])
    writer.writerow(['Sanada', '56', 'Kyoto'])

def csv_dict(filepath: str) -> List[Dict]:
    try:
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            X = []
            for i in reader:
                if int(i[1]) >= 40:
                    X.append({'name': i[0], 'age'git: int(i[1]), 'city': i[2]})
            return X
    except FileNotFoundError as e:
        print(f'ファイルが見つかりませんでした: {e}')
    finally:
        print('csv変換処理が終了しました！')

def dict_json(data: List[Dict], filepath: str) -> None:
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print(f'予期せぬエラーが起こりました: {e}')
    finally:
        print('json変換処理が終了しました！')

if __name__ == '__main__':
    dict_json(csv_dict('people.csv'), 'out_put_3.json')