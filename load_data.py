import csv

def load_csv_file(filename):
    nft_data = []
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            nft_data.append(row)
    
    return nft_data