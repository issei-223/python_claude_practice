import pandas as pd
import csv

def analyze(df: pd.DataFrame) -> pd.DataFrame:
    try:
        result = df.groupby('category')['sales'].agg(
            total_sales = 'sum', 
            avg_sales = 'mean',
            max_sales = 'max',
        )
        return result.round(2)
    except FileNotFoundError as e:
        print(f'ファイルが見つかりませんでした: {e}')
    finally:
        print('データ処理が完了しました')

if __name__ == '__main__':
    df = pd.read_csv('sales.csv')
    analyze(df).to_csv('report.csv', index=True)