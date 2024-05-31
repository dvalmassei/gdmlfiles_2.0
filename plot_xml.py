#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 09:19:04 2024

@author: danielvalmassei
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    df = pd.read_xml('mainDetmatrices.xml')
    
    
    for j in range(len(df['name'])):
        array = np.char.lstrip(np.array(df['values'][j].split('    '))).tolist()
        energy = np.zeros(len(array)-1)
        value = np.zeros(len(array)-1)
        for i in range(len(array)-1):
            temp = array[i+1].split(' ')
            energy[i] = float(temp[0].split('*')[0])
            value[i] = float(temp[1].split('*')[0])        
        

        plt.scatter(energy,value)
        plt.xlabel('Energy [eV]')
        plt.title(df['name'][j])
        plt.savefig(df['name'][j] + '.png')
        plt.show()
    
if __name__ =='__main__':
    main()