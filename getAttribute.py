import hachoir
import subprocess
import datetime
import os
from os import listdir
from os.path import isfile, join

def get_media_properties(filename):

    result = subprocess.Popen(['hachoir-metadata', filename, '--raw', '--level=9'],
        stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

    results = result.stdout.read().decode('utf-8').split('\r\n')

    for item in results:
        if '- creation_date:' in item:
            return(item[16:])

def change_tittle(path,newTittle, oldTittle):
    newTittle = newTittle.replace(':','-')
    os.rename(path+oldTittle,path+newTittle)

def getFilesName(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    return onlyfiles

def changeAllFilesInPath(path):
    filesName = getFilesName(path)
    for i in filesName:
        print(i)
        try:
            newTittle = get_media_properties(path+i)
            change_tittle(path,newTittle+".mp4",i)
        except:
            continue

path = input("Input path: ")
changeAllFilesInPath(path)