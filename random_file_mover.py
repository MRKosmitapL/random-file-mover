import os
import argparse
import random
from collections import Counter
import shutil

def merge_sort(tablica): #cuz I'm bored
    if len(tablica) < 2:
        return tablica
    srodek = len(tablica) // 2
    lewa_polowa = tablica[:srodek]
    prawa_polowa = tablica[srodek:]
    lewa_polowa = merge_sort(lewa_polowa)
    prawa_polowa = merge_sort(prawa_polowa)
    return merge(lewa_polowa, prawa_polowa)

def merge(lewa, prawa):
    wynik = []
    i = 0 
    j = 0 
    while i < len(lewa) and j < len(prawa):
        if lewa[i] < prawa[j]:
            wynik.append(lewa[i])
            i += 1
        else:
            wynik.append(prawa[j])
            j += 1
    wynik.extend(lewa[i:])
    wynik.extend(prawa[j:])
    return wynik

parser = argparse.ArgumentParser(description="Moves random files from one folder to second")
parser.add_argument("-n","--number", help="input the number of files you want to move", required=True)

source_folder = ""
source_folder_files = os.listdir("")
target_folder = ""
file_extension = '.webm'

files = []
files += [each for each in source_folder_files if each.endswith(file_extension)]
usedFiles = []
args = vars(parser.parse_args())
number_of_files = int(args['number'])
dupacounter = 0
for i in range(0,number_of_files):
    x = random.randint(0,99)
    if x in usedFiles:
        while x in usedFiles:
            x = random.randint(0,99)
            
    usedFiles.append(x)
    
duplicates = [item for item, count in Counter(usedFiles).items() if count > 1]
usedFiles = merge_sort(usedFiles)
i = len(usedFiles)-1
while(i >= 0):
    index = usedFiles[i]
    shutil.move(source_folder+"/"+files[index], target_folder)
    i-=1
