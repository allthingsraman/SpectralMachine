#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
*********************************************
* Show classes in Learning dataset.
* version: 20231214a
* By: Nicola Ferralis <feranick@hotmail.com>
***********************************************
'''
print(__doc__)
import numpy as np
import sys, os.path, random, h5py
import matplotlib.pyplot as plt

def main():
    if(len(sys.argv)<2):
        print(' Usage:\n  python3 ShowClasses.py <learnData>\n')
        print(' Requires python 3.x. Not compatible with python 2.x\n')
        return

    En, M, Cl, learnFileRoot = readLearnFile(sys.argv[1])
    
    print(" Number of spectra in dataset:",Cl.shape[0])
    print(" Number of unique classes in dataset:",np.unique(Cl).shape[0])
    if Cl.shape[0] - np.unique(Cl).shape[0] > 0:
        print(" Classes with multiple data present.")
    print("\n Unique classes in learning/validation set:\n")
    with np.printoptions(threshold=np.inf):
        print(np.unique(Cl).astype(int),"\n")
        
#************************************
''' Open Learning Data '''
#************************************
def readLearnFile(learnFile):
    print(" Opening learning file: "+learnFile+"\n")
    try:
        if os.path.splitext(learnFile)[1] == ".npy":
            M = np.load(learnFile)
        elif os.path.splitext(learnFile)[1] == ".h5":
            with h5py.File(learnFile, 'r') as hf:
                M = hf["M"][:]
        else:
            with open(learnFile, 'r') as f:
                M = np.loadtxt(f, unpack =False)
    except:
        print("\033[1m" + " Learning file not found \n" + "\033[0m")
        return
    
    learnFileRoot = os.path.splitext(learnFile)[0]
    En = M[0,1:]
    A = M[1:,1:]
    Cl = M[1:,0]
    return En, A, Cl, learnFileRoot

#************************************
''' Main initialization routine '''
#************************************
if __name__ == "__main__":
    sys.exit(main())