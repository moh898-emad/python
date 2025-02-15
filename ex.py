lst=[]
for i in range(5) :
    a=input("enter event num")
    lst.append(a)

def x(my_list):
    for i in my_list :
        if (i %2==0):
         print(i)

        x(lst)