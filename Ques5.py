# Q5.Write a python program to check if all items in a tuple are the same?
t1=("mysirg","mysirg","mysirg")
result=t1.count(t1[0])==len(t1)
if result:
    print("Equal")
else:
    print("Non Equal")

