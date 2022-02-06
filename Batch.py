from lister import listgetter
from Filepaths import *
from Inserter import *
def Batch():
    address=str(input("Enter the address"))
    if address[0]=='"':
        address=address[1:-1]
    print('ffffffffffffffffffff')
    names,og = get_filepaths(address)
    print (names+og)
    try:
        l=listgetter(names)
        pictureInserter(og,address,l)
    except TypeError:
        print("Incorrect name")
    

if __name__ == "__main__":
    Batch()