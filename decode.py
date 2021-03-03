from os import EX_DATAERR
from typing import Awaitable


with open("string.txt", "r") as file:
    data=file.read()

# data.replace(',','')

alpha_dict = {}
[alpha_dict.update({x:data.count(x)}) for x in data]
alpha_list = list(alpha_dict.values())
max(sorted(alpha_list))
sorted(alpha_dict)


# What is the letter that is most frequent? This most likely will be our E since it is a very common letter.
[x for x in alpha_dict if alpha_dict[x] == 15]


##### ----- TRYING THINGS ----------
# key = {'F':'H',\
#     'E':'F',\
#     'M':'T',\
#     'P':'R',\
#     'Q':'G',\
#     'R':'E',\
#     'T':'I',\
#     'V':'0',\
#     'X':'N'}


# F='H'
# E='F'
# M='T'
# P='R'
# Q='G'
# R='E'
# T ='I'
# # V= 'N'
# A = 'I'
# D = 'S'
# X = 'N'
# G = 'A'
# V ='O'

# {'F':'H'}

# data.replace('F',F)\
#     .replace('E',E)\
#     .replace('M',M)\
#     .replace('R',R)\
#     .replace('P',P)\
#     .replace('A',A)\
#     .replace('D',D)\
#     .replace('X',X)\
#     .replace('G',G)\
#     .replace('V',V)
    


# for x in key:
#     print(data) 
#     data=data.replace(x,key[x])
#     print(data)
    

# 'AA'
# 'BB'
# 'CC'
# 'DD'
# 'EE'


# test = map('abc','def')
# test
#### ----------------END TRYING THINGS ------------------

new_list = list(range(len(data)))

alpha_dict={',':',',
    ' ':' ',
    'F':'H', 
    'E':'F',
    'M':'T',
    'P':'R',
    # 'Q':'G',\
    'R':'E',
    # 'T':'I',\
# V= 'N'
    'A':'I',
    'D': 'S',
    'X' : 'N',
    'G' : 'A', 
    'V' :'O',
    'K': 'U',
    'H': 'C',
    'Z':'G'}


data_dict = {i:x for i,x in enumerate(data)}

for p in alpha_dict:
    for k,v in data_dict.items():
        if v == p:
            new_list[k]=alpha_dict[p]

new_list

print(*new_list,sep='')
print(data)