# Edgar Barrera / Github: https://github.com/EdgarCastillo101/EdgarCastillo101
# Copyright (c) 2021 Edgar Barrera

import pickle

def storeData():
    # initializing data to be stored in db
    Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 'age' : 21, 'pay' : 40000}
    Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak', 'age' : 50, 'pay' : 50000}

    # database
    db = {}
    db['Omkar'] = Omkar
    db['Jagdish'] = Jagdish

    dbfile = open('examplePickle', 'ab')        # Its important to use binary mode
    pickle.dump(db, dbfile)                     # source, destination
    dbfile.close()

def loadData():
    dbfile = open('examplePickle', 'rb')        # for reading also binary mode is important
    db = pickle.load(dbfile)
    for keys in db:
        print(keys,'=>',db[keys])
    dbfile.close()

if __name__ == '__main__':
    storeData()
    loadData()
