#python program to find highest 3 values in dictionary

from heapq import nlargest
a={'a':7889,'b':5332,'c':8645,'d':6778,'e':5789}
b=nlargest(3,a,key=a.get)
print(b)

Output
['c', 'a', 'd']