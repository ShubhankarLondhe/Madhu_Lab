import csv
import os

dirc = 'uniq_comb/'

f = open('unique_stars.csv','w')
w = csv.writer(f)

ls = ['Central Group', 'Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5', 'Group 6']
w.writerow(ls)

for file in os.listdir(dirc):
    if file.endswith(".csv"):
        name = file[4:]
        cent = int(name[:-4])
        with open(dirc+file, 'r') as g:
            r = csv.reader(g)
            for line in r:
                temp = []
                temp.append(cent)
                ls = [int(i) for i in line]
                temp.extend(ls)
                w.writerow(temp)
                
f.close() 