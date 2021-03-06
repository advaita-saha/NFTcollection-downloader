from get_nft import get_nft_collection
from download import download_collection
from load_data import load_csv_file
import csv

print("1: Load data from csv file and download images")
print("2: Scan a NFT collection to retrieve data")
choice1 = int(input('Enter the option number you want to perform : '))

if choice1 == 1:
    csv_filename = input('Enter the path for the csv file : ')
    nft_collection = load_csv_file(csv_filename)
    download_collection('untitled', nft_collection)
elif choice1 == 2:
    nft_address = input("Enter the NFT's contract address to retrieve all the data : ")
    fields = ['id', 'link']
    nft_collection = get_nft_collection(nft_address)
    filename = 'nft_data_{}.csv'.format(nft_address)

    print("1: Save data to csv file")
    print("2: Download images")
    choice = int(input('Enter the option number you want to perform : '))

    if choice == 1:
        with open(filename, 'w+') as csvfile: 
            writer = csv.DictWriter(csvfile, fieldnames = fields) 
            writer.writeheader() 
            writer.writerows(nft_collection) 
        print('Data succesfully written to a file : {}'.format(filename))
    elif choice == 2:
        download_collection(nft_address, nft_collection)
    else:
        print('Sorry Unknown Option, Bye')