import csv
import sys
import os
import numpy as np

db_file_loc = sys.argv[1]
split_dir = sys.argv[2]

ls = ['GPDB#','Central Group','x','y','z','Group1','x1','y1','z1','Group2','x2','y2','z2','Group3','x3','y3','z3','Group4','x4','y4','z4','Group5','x5','y5','z5','Group6','x6','y6','z6']
name = os.path.basename(db_file_loc)
db_file = split_dir + name

f1 = open('%s_sp1.csv'%db_file,'w')
w1 = csv.writer(f1)
w1.writerow(ls)

f2 = open('%s_sp2.csv'%db_file,'w')
w2 = csv.writer(f2)
w2.writerow(ls)

f3 = open('%s_sp3.csv'%db_file,'w')
w3 = csv.writer(f3)
w3.writerow(ls)

f4 = open('%s_sp4.csv'%db_file,'w')
w4 = csv.writer(f4)
w4.writerow(ls)

f5 = open('%s_sp5.csv'%db_file,'w')
w5 = csv.writer(f5)
w5.writerow(ls)

with open(db_file_loc,'r') as db:
    r = csv.reader(db)
    next(r)
    for line in r:
        rn = np.random.uniform(0,1)
        if rn<0.2:
            w1.writerow(line)
        elif 0.2<=rn and rn<0.4:
            w2.writerow(line)
        elif 0.4<=rn and rn<0.6:
            w3.writerow(line)
        elif 0.6<=rn and rn<0.8:
            w4.writerow(line)
        else:
            w5.writerow(line)


f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
