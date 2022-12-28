#add two no by lamda function
# lambda_add_no=lambda x,y: x+y

# # y1=10
# # y2=20
# y1='hi'
# y2=" how are you"

# print(lambda_add_no(y1,y2))

#concat two string
#normal function to calculate max between two
# def max_of_two_no(a,b):
#     if a>b:
#         return a
#     else:
#         return b


# print("the no is",max_of_two_no(40,60))   

# list1=[1,2,3,4,5,7,5,6,7]
# square_num=lambda x:x*x
# square_list= list(map(square_num,list1))
# set1=set()
# set1.update(square_list)
# print(set1)

list2=[1,3,2,1,4]
list1=[1,2,3,4,5]
# # list3=list1+list2
# # print(list3)

# add_list=lambda x,y:x+y
# add_map=list(map(add_list,list1,list2))
# print(add_map)

filter_abc=lambda x:x%2==0

result=list(filter(filter_abc,list2))
print(result)



            



