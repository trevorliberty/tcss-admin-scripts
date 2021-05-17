import sys
import os
import subprocess
import shutil
from datetime import date

notes = []

kw = '__MACOSX'

def extractTar(filename, folder):
    os.chdir(folder)
    subprocess.run(['tar', '-xvf', f"../{filename}"])
    findAndRemove__MACOSX()
    os.chdir('../')

def extractZip(filename, folder):
    os.chdir(folder)
    subprocess.run(['unzip', f"../{filename}"])
    findAndRemove__MACOSX()
    os.chdir('../')

def extractZipDest(filename,folder):
    subprocess.run(['unzip', filename, "-d", folder])

def findAndRemove__MACOSX():
    if kw in os.listdir():
        shutil.rmtree(kw)

def findTarfile(type):
    if type.find('.tar') >= 0 or type.find('.gz') >=0:
        return True
    return False


def run(startfolder):
    os.chdir(startfolder)
    files = os.listdir()
    for f in files:
        type = f[f.rindex('.'):]
        if findTarfile(type):
            dirname = f[:f.find('_')]
            os.mkdir(dirname)
            extractTar(f, dirname)
        elif type.find('.zip') >=0:
            dirname = f[:f.find('_')]
            try:
                os.mkdir(dirname)
            except:
                os.mkdir(f"{dirname}-1")
            extractZip(f, dirname)
        else: 
            notes.append(f"{f} is not a zipfile or tar file\n")
    # [os.remove(x) for x in os.listdir() if (x.find('.tar') or x.find('.zip'))]
    for file in list(filter(lambda x: x.find('.tar')>=0 or x.find('.zip')>=0, os.listdir())):
        os.remove(file)

def writeout():
    with open("notes.txt", "w") as f:
        notes.sort()
        notes.insert(0, '*******NOTES*******\n')
        f.writelines(notes)
try: 
    zipfile = 'submissions.zip'
    cwd = os.getcwd()
    try: 
        zipfile = sys.argv[1]
    except: 
        print('f')
    startfolder = str(date.today())
    os.mkdir(startfolder)
    extractZipDest(zipfile, startfolder)
    run(startfolder)
    os.chdir(cwd)
    writeout()
except Exception as e:
   print(e) 