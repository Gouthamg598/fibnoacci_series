
''' ==============anagram==========='''
a='listen'
b='silent'
a=sorted(a)
b=sorted(b)
if a==b:
    print("anagram")
else :
    print('not anagram')

'''==================='''
a='list'
b='tils'
a="raagdk"
b='hskfh'
x=[a[i] for i in range(0,len(a))]
x.sort()

y=[b[i] for i in range(0,len(b))]
y.sort()

if (x==y):print("anagram")
else:print('not anagram')

'''========================='''
def anagram(str1,str2):
    a=sorted(str1)
    b=sorted(str2)
    if a==b:
        print('anagram')
    else:
        print('not an anagram')
anagram('sound','listen')#not an anagram
anagram('listen','silent')#anagram
