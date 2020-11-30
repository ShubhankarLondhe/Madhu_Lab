# Frequency for each pair of AAs with one of them as group2

import os
import numpy as np

def make_pair(a,b):
    if a != 2:
        ind = a-1
    else:
        if b in [3,5,9,13,14,15,16]:
            ind = b-1
        elif b == 2:
            ind = 1
        elif b == 6:
            ind = 16
        elif b == 8:
            ind = 17
        elif b == 12:
            ind = 18 
    return ind


def freq(dirc):
    count = np.zeros((19,))
    
    for file in os.listdir(dirc):
        if file.endswith('.gpdb'):
            f = open(dirc+file,'r')
            f_r = f.readlines()
            for i in range(len(f_r)-1):
                l0 = f_r[i]     #list(f_r[i])
                l1 = f_r[i+1]   #list(f_r[i+1])
                if l0[:4] == 'ATOM' and l1[:4] == 'ATOM':
                    a = int(l0[13:15]); b = int(l1[13:15]) 
                    indx = make_pair(a,b)
#                     print(a,b,indx)
                    
                    count[indx]+=1
                    if a == 2 and b != 2:
                        i+=1
            f.close()
    return count

dirc = 'temp_shubhankar_starsDBcreator/starfinder/'
print(freq(dirc))