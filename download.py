import requests
from halo import Halo
import os

ipfs_gateway = "https://gateway.moralisipfs.com/ipfs/"

@Halo(text='Downloading all the NFT images, have a coffee till then', spinner='dot')
def download_collection(name, collection):

    for i in collection:
        url = ipfs_gateway+i['link'][7:]
        filename = name+'/{}.png'.format(i['id'])
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        f = open(filename,'wb')
        f.write(requests.get(url).content)
        f.close()

    print('Download Completed of {} images from collection {}'.format(len(collection), name))