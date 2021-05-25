# Edgar Barrera / Github: https://github.com/EdgarCastillo101/EdgarCastillo101
# Copyright (c) 2021 Edgar Barrera

import csv

def csvRead(filePath):
    with open(filePath) as fd:
        reader = csv.reader(fd, delimiter = ',')
        for row in reader:
            print(row[0] + ' ' + row[1])

def csvWrite(filePath, data):
    with open(filePath, 'a') as fd:
        writer = csv.writer(fd, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(data)

if __name__ == '__main__':
    # data = ['Firstname', 'Lastname']
    # csvWrite('example.csv', data)
    userInput = input('What is your Fullname? ')
    userInput = userInput.split(' ')
    csvWrite('example.csv', userInput)
    csvRead('example.csv')
