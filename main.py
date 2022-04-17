from dataclasses import field
from traceback import print_tb
from get_nft import get_nft_collection
import csv

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
    print('Sorry!! Support coming soon!!')
else:
    print('Sorry Unknown Option, Bye')