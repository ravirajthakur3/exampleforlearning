num1=int(input("enter the no ="))
a=0
b=1
count=0
if num1==0:
    print("please enter valid no")
elif num1==1:
    print(a)
else:
    # print(a)
    # print(b)
    # for i in range(2,num1):
    #   temp=a+b
    #   a=b
    #   b=temp
    #   print(temp)
     
    # for i in range(0,num1):
    #   print(a)
    #   c=a+b
    #   a=b
    #   b=c
   while count<num1:
    print(a)
    c=a+b
    a=b
    b=c
    count +=1


