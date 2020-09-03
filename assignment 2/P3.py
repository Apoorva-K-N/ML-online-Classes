#python program to count number of elements in a list within specified range

n=int(input("Enter the size of list"))
a=[]
b=[]
for i in range(n):
    a.append(input())
x=int(input("Enter the 1st range"))
y=int(input("Enter the 2nd range"))
for i in range(x,y+1):
    b.append(a[i])
print(b)

Output
Enter the size of list 5
1
3
4
2
5
Enter the 1st range 1
Enter the 2nd range 3
['3', '4', '2']