import csv
import numpy as np

grp_ind = [5,9,13,17,21,25]

def make_row(line):
    row = []
    for i in range(29):
        if i in grp_ind:
            row.append(int(line[i]))
    row.sort()
    return row


# grp = central group #, pass 'grp' as an int
def check_comb(file, row):
    row = [str(i) for i in row]
    with open(file,'r') as f:
        r = csv.reader(f)
        c = 0
        for line in r:
            if row == line:
                c = 1
                break
        if c == 1:
            return 1   # Row present 
        else:
            return 0   # Row not present
            

with open('sample_db.csv', 'r') as f:
    r = csv.reader(f)
    next(r)
    for line in r:
        ls = list(line)
        cent_grp = int(ls[1])
        file = "uniq_comb/grp_%s.csv"%cent_grp
        g = open(file,'a')
        row = make_row(ls)
        if check_comb(file,row) == 0:
            w = csv.writer(g)
            w.writerow(row)
        
        g.close()
        
        