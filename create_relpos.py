import csv
import time
import numpy as np

start_time = time.time()

gr_index = np.array([5,9,13,17,21,25])

def rel_pos(ls):
    rel_vec = []
    rel_vec.extend(ls[0:2])
    for i in gr_index:
        temp = []
        temp.append(ls[i])
        for j in gr_index:
            coor = []
            if i!=j:
                coor.append(round(float(ls[i+1])-float(ls[j+1]),3))
                coor.append(round(float(ls[i+2])-float(ls[j+2]),3))
                coor.append(round(float(ls[i+3])-float(ls[j+3]),3))
                temp.extend(coor)
        rel_vec.extend(temp)
    return rel_vec


# Create header row
ls = ['GPDB #','Central Group']
for i in range(1,7):
    ls.append('Group%s'%i)
    for j in range(1,7):
        if i!=j:
            ls.extend(['x_%s_%s'%(i,j),'y_%s_%s'%(i,j),'z_%s_%s'%(i,j)])
    


f = open("/home/madhu/shubhankar/stars_NRaa_nr30.csv","r")
r = csv.reader(f)
g_rel = open("/home/madhu/shubhankar/stars_NRaa_nr30_relpos.csv","w")
w_rel = csv.writer(g_rel)
w_rel.writerow(ls)
next(r)
for line in r:
    w_rel.writerow(rel_pos(line))

f.close()
g_rel.close()
print("--- %s seconds ---" % (time.time() - start_time))