#python program to remove duplicate elements from list

n=int(input("Enter the size of list "))
a=[]
for i in range(n):
    a.append(input())
b=set(a)
print(list(b))

Output
Enter the size of list 4
1
we
3
we
['3', '1', 'we']