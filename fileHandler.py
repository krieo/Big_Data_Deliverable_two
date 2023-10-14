import csv


def read_csv_file(file_path):
    data = []
    with open(file_path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data
