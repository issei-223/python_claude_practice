import csv

with open('sales.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['date', 'product', 'category', 'sales', 'quantity'])
    writer.writerow(['2024-01-01', 'Apple', 'Food', '1500', '10'])
    writer.writerow(['2024-01-01', 'Notebook', 'Stationery', '800', '5'])
    writer.writerow(['2024-01-02', 'Apple', 'Food', '2000', '15'])
    writer.writerow(['2024-01-02', 'Pen', 'Stationery', '300', '20'])
    writer.writerow(['2024-01-03', 'Banana', 'Food', '1200', '8'])
    writer.writerow(['2024-01-03', 'Notebook', 'Stationery', '1600', '10'])






