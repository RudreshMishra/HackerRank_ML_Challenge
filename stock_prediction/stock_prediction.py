'''
This code is to solve the challenge at the hacker rank
https://www.hackerrank.com/challenges/stockprediction
'''

#!/usr/bin/py
import sys
import numpy as np
import math
def printTransactions(m, k, d, name, owned, prices):
    slope_list=[]
    for i in range(k):
        x=np.array([1.0,2.0,3.0,4.0,5.0])
        y= np.array(prices[i])
        A = np.vstack([x, np.ones(len(x))]).T
        slope, constat = np.linalg.lstsq(A, y)[0]
        slope_list.append(slope)
    sort_slope = sorted(slope_list)
    amount_remaining= m
    trans={}

    for j in reversed(range(k)):
        index_slope = slope_list.index(sort_slope[j])
        if sort_slope[j]<=0 and amount_remaining>=prices[index_slope][-1]:
            num_stock =math.floor(amount_remaining/prices[index_slope][-1])
            amount_remaining = amount_remaining - prices[index_slope][-1]*num_stock
            trans[name[index_slope]] = names[index_slope]+' BUY ' + str(int(num_stock))

    for j in range(k):
        index_slope = slope_list.index(sort_slope[j])
        if sort_slope[j]>0 and owned[index_slope]>0:
            trans[name[index_slope]] = names[index_slope]+' SELL ' + str(owned[index_slope]) 

    print (len(trans.keys()))
    for x in trans:
        print(trans[x])

def expand_arg_files(args):
    for arg in args:
       if arg.startswith('@'):
           with open(arg[1:]) as f:
               file_args = f.read().splitlines()
           yield from expand_arg_files(file_args)
       else:
           yield arg
if __name__ == '__main__':
    sys.argv[:] = expand_arg_files(sys.argv[:])
    m, k, d = [float(i) for i in sys.argv[1].strip().split()]
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    # print(sys.argv)
    for data in range(k):
        temp = sys.argv[data+2].strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])
    printTransactions(m, k, d, names, owned, prices)