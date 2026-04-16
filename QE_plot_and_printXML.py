#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:10:27 2026

@author: danielvalmassei
"""

import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('seaborn-v0_8')
df1 = pd.read_csv('~/Downloads/9305KB_qe.csv')
df1 = df1.sort_values(by='wavelength',ascending=False)

df2 = pd.read_csv('~/Downloads/r375_qe.csv')
df2 = df2.sort_values(by='wavelength',ascending=False)

df3 = pd.read_csv('~/Downloads/9305QKB_qe.csv')
df3 = df3.sort_values(by='wavelength',ascending=True)



plt.scatter(df1['wavelength'],df1['QE'],s=20,marker='.',label='ET 9305KB')
plt.scatter(df3['wavelength'],df3['QE'],s=20,marker='s',label='ET 9305QKB')
plt.scatter(df2['wavelength'],df2['QE'],s=20,marker='^',label='Hamamatsu R375')

plt.ylabel('Quantum Efficiency %')
plt.xlabel('Wavelength (nm)')
plt.legend()
plt.yscale('log')
plt.show()


'''
length = len(df3['wavelength'])
for i in range(length):
    print(f'{1239.8/df3['wavelength'][length-i-1]:.6f}*eV {df3['QE'][length-i-1]:.6f}')
'''

length = len(df2['wavelength'])
for i in range(length):
    print(f'{1239.8/df2['wavelength'][length-i-1]:.6f}*eV {df2['QE'][length-i-1]:.6f}')
    
'''
length = len(df1['wavelength'])
for i in range(length):
    print(f'{1239.8/df1['wavelength'][length-i-1]:.6f}*eV {df1['QE'][length-i-1]:.6f}')

'''