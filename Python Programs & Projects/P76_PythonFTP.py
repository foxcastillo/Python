# Edgar Barrera / Github: https://github.com/EdgarCastillo101/EdgarCastillo101
# Copyright (c) 2021 Edgar Barrera

import ftplib

def ftp_upload(ftpObj, pathToSend, pathToRecv, fileType='TXT'):
    """
    A function for uploading files to an FTP server
    @param ftpObj: The file transfer protocol object
    @param path: The path to the file to upload
    """
    with open(pathToSend, 'rb') as fobj:
        ftpObj.storlines('STOR ' + pathToRecv, fobj)

if __name__ == '__main__':
    ftp = ftplib.FTP('127.0.0.1')
    ftp.login('omkarpathak', '8149omkar')
    print('Logged in..')

    pathToSend = '/home/omkarpathak/Desktop/output.txt'
    pathToRecv = '/home/omkarpathak/Documents/output.txt'
    ftp_upload(ftp, pathToSend, pathToRecv)

    ftp.quit()
