# list1=[1,3,2,3,4,5,'ravi','raj','ravi']
# set1=set(list1)
# print(list(set1))
# set2={1,2,3,4,5,2,2,1,1,9,8}
# set3={1,2,3,4,4,5,9,8}
# print(set2==set3)

#factorial of a no
# def factorial(a):
#     result=1
#     if a==0 :
#       return 1 
#     if a==1:
#       str1='hello'
#       return str1
#     else:
          
#       for fac_result in range(1,a+1):
#         result=result*fac_result
#         print(result)
#     return result    
    
# num=20
# output1=factorial(num)   
# print(output1)  

def sqare_cube(n):
    square=n*n
    cube=n*n*n
    return square,cube

num=2
output2,out3=sqare_cube(num)
print("square",output2)
print("cube",out3)



    