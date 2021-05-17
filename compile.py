import sys
import glob
import subprocess
import os
from os.path import isdir

lines = []


def checkFiles():
    if isdir(os.listdir()[0]): 
        os.chdir(os.listdir()[0])


def compile(folder):
    if 'a.out' in os.listdir():
        os.remove('a.out')
    os.chdir(folder)
    checkFiles()
    run = ["g++"] + glob.glob("*.cpp")
    subprocess.run(run)
    if len(glob.glob("a.out")) > 0: 
        return True
    return False

def appendResults(name, result):
    print(f"{name}: {result}")
    lines.append(f"{name}, {result}\n")

def run(fpath):
    os.chdir(fpath)
    filepath = os.getcwd()
    for folder in os.listdir():
        try:
            if compile(folder):
                appendResults(folder, "pass")
            else: 
                appendResults(folder, "fail")
        except Exception as e:
            print(e)
        os.chdir(filepath)


try: 
    fpath = sys.argv[1]
    run(fpath)
    os.chdir('../')
    with open("results.txt", "w") as f:
        lines.sort()
        f.writelines(lines)
except Exception as e:
    print("STACKTRACE")
    print(e)

