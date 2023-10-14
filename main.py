import fileHandler

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_path = "phase2_train_v0.csv"
    csv_data = fileHandler.read_csv_file(file_path)
    i = 0
    for row in csv_data:
        print(row)
        print(i)
        i += 1


