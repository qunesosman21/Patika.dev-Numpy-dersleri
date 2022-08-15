"""
hackrank numpy min ve max örneği
link: https://www.hackerrank.com/challenges/np-min-and-max/problem

"""

import numpy as np

n,m=map(int,input().split())

arr = np.array([list(map(int,input().split())) for i in range(n)])

print(max(np.min(arr,axis=1)))
