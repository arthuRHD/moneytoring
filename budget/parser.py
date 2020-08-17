import csv
import os
from datetime import datetime

csv_file_path = os.path.join(os.path.dirname(__file__), "transactions.csv")

reader = csv.reader(open(csv_file_path))


def print_raw_data():
    data = [row for row in reader]
    for row in data:
        print(row)


def get_parsed_data():
    parsed_data = []
    lines = [line for line in open(csv_file_path)]
    for line in lines:
        if line != lines[0]:
            listed = line.strip().replace(',', '.').split(';')
            date = datetime.strptime(listed[0], '%d/%m/%Y')
            type_transaction = listed[2]
            montant = float(listed[5])
            dest = listed[7]
            parsed_data.append([date, type_transaction, montant, dest])
    return parsed_data
