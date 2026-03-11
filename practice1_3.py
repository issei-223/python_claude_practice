import csv
import json
from typing import List, Dict

with open('users.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Alice','30', 'Tokyo'])
    writer.writerow(['Bob','25', 'Osaka'])
    writer.writerow(['Carol','28', 'Nagoya'])
    writer.writerow(['Diana','17', 'Sapporo'])
    writer.writerow(['Eve','35', 'Fukuoka'])

def  read_csv(filepath: str) -> List[Dict]:
    try:
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            X = []
            for i in reader:
                if int(i[1]) >= 18:
                    X.append({'name': i[0], 'age': int(i[1]), 'city': i[2]})
            return X
    except FileNotFoundError as e:
        print(f'ファイルが見つかりませんでした: {e}')
    finally:
        print('csv変換処理が終了しました')

def save_json(data: List[Dict], filepath: str) -> None:
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print(f'予期せぬ事態が起こりました: {e}')
    finally:
        print('json変換処理を終了しました')

if __name__ == '__main__':
    save_json(read_csv('users.csv'), 'out_put_2.json')