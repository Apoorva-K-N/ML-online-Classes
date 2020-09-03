#python program to count number of occurences of a word in the sentence

a=str(input("Enter the sentence: "))
b=dict()
c=a.split()
for i in c:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)

Output
Enter the sentence: i love my nation and also i love my state
{'i': 2, 'love': 2, 'my': 2, 'nation': 1, 'and': 1, 'also': 1, 'state': 1}
    