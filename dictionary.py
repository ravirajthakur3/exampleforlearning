# dict1={}
# dict1['name']='raviraj'

# list=[]
# list.append(22)
# list.append('ravi')
# dict1['age']=23
# #
# # print("dict1",dict1,"list",list)
# dict3={'name':'ram','nationality':'ndian' 'pak'}
# #dict1['other_details']=dict3
# dict1['list_details']=list
# temp=dict3['nationality']
# print(temp[1])



# #print(list[0])
# #print(dict1,"and")
# #print(len(dict1))
# print

# print(dict3['name'][1])
# dict4={}
# dict4['skills']=['python','c++']
# print(dict4['skills'][1])
# print(dict1)
# print(dict1['list_details'])
# dict1['extra_skills']=dict4
# print(dict1)
# print(dict1['extra_skills']['skills'])
dict5={'name':'ravi','age':'24','title':'thakur'}
# for k,v in dict5.items():
#     print(k,'and',v)

# #del dict5['age']   
# print(dict5) 
# dict6={'gender':'male','married':'no'}
# dict6['extra']='education'
# dict5['ectra_row']=dict6
# print(dict5)
# del dict5['name']
# del dict6['gender']
# del dict5['ectra_row']
# print(dict5)
keys_found=dict5.keys()
print(keys_found)
if 'name' in keys_found:
    print('true')
else:
    print("false")    
print(list(keys_found))
