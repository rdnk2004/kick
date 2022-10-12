#Given a list i=[22,45,33,45,21,19,19,13,22,45].Find how many times the number 45 is repeated and print the same.
count=0
l=[22,45,33,45,21,19,19,13,22,45]
for i in l:
    if(i==45):
        count=count+1
print(count)
