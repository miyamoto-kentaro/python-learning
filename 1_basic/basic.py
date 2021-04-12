print('#'*10,'Definition','#'*10)
# 上のprintは考えなくてよい...  出力結果の見栄えをよくするために[########## Definition ##########]と区切っている。
""" ... コメントアウト
Definition
"""
# you can define any variables like this
var1 = 'hello'
var2 = 'python'
# var1 contain hello and var2 contain python
print(var1,var2)
# function called print process output valiable in console

# ------------------------------------------------------------------------------------------------------ #

print('#'*10,'Any Types','#'*10)
"""
Any Types
"""
# variable has types like int float str list tupl ...
# we can check the type like this
var3 = 3.14
var4 = [1,2,3,4]
print('var1 is',type(var1))
# output -> str 
# it mean var1 is string
# more process ...
print('var2 is',type(var2))
print('var3 is',type(var3))
print('var4 is',type(var4))
# we can translate type to other type like this
var5 = 8080
var6 = str(var5)
print(var5,'is',type(var5),'and',var6,'is',type(var6))

# ------------------------------------------------------------------------------------------------------ #

print('#'*10,'If Process','#'*10)
'''
If Process
'''
# you maybe know the 'if' process
if True:
    print('output','True')
if False:
    print('output','False')
# console popout only True, it mean 'if' process is pass through only True object
# look at a type of True and False
print('True is',type(True))
print('False is',type(False))
# output bool, bool mean Boolean. bool has True or False
# other type like int, float, string... can be translated to bool type like this
print(var1,'is',bool(var1))
print('blank is',bool(''))
print(1,'is',bool(1))
print(0,'is',bool(0))
# else get False object
if False:
    print('get True')
else:
    print('get False')
# let's try Color Guessing Game.
# :which color would output
if 0:
    if '':
        print('color game:red')
    else:
        print('color game:blue')
else:
    if 'False':
        print('color game:yellow')
    else:
        print('color game:green')

# ------------------------------------------------------------------------------------------------------ #

print('#'*10,'For Process','#'*10)
'''
For Process
'''
# you maybe know the for process
for item in var4:
    print('number',item)
# var4 object has [1,2,3,4]
# for process get item one by one from var4

print('#'*10,'While process','#'*10)
'''
While process
'''
# you maybe know the while process
# so while process is running during true
num = 0
while num<3:
    print('num is',num,',so this is smaller than 3')
    num += 1
