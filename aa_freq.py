# Frequency for each pair of AAs with one of them as group2

import os
import numpy as np

def make_pair(a):
    if a == 'ALA':
        ind = 0
    elif a == 'ARG':
        ind = 1
    elif a == 'ASN':
        ind = 2
    elif a == 'ASP':
        ind = 3
    elif a == 'CYS':
        ind = 4
    elif a == 'GLU':
        ind = 5
    elif a == 'GLN':
        ind = 6
    elif a == 'GLY':
        ind = 7
    elif a == 'HIS':
        ind = 8
    elif a == 'ILE':
        ind = 9
    elif a == 'LEU':
        ind = 10
    elif a == 'LYS':
        ind = 11
    elif a == 'MET':
        ind = 12
    elif a == 'PHE':
        ind = 13
    elif a == 'PRO':
        ind = 14
    elif a == 'SER':
        ind = 15
    elif a == 'THR':
        ind = 16
    elif a == 'TRP':
        ind = 17
    elif a == 'TYR':
        ind = 18
    elif a == 'VAL':
        ind = 19
    return ind
    
        
def freq(dirc):
    count = np.zeros((19,))
    
    for file in os.listdir(dirc):
        if file.endswith('.gpdb'):
            f = open(dirc+file,'r')
            f_r = f.readlines()
            for i in range(len(f_r)-1):
                l0 = f_r[i]     #list(f_r[i])
                if l0[:4] == 'ATOM':
                    aa = l0[17:20]
                    indx = get_ind(a)
#                     print(a,b,indx)
                    count[indx]+=1
                    
                    if ind in [0,3,4,8,15]:
                        i+=1
                    elif ind in [2,5,12,13,16,17,18]:
                        i+=2
                    elif ind in [1,6,19]:
                        i+=3
                    elif ind in [9,10,11]:
                        i+=4
            f.close()
    return count

dirc = 'temp_shubhankar_starsDBcreator/starfinder/'
print(freq(dirc))