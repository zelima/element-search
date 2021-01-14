# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html

# User gives list of [1,4,5,12,16,45] and Number 120 as an input.
# User gives list of [1,4,5,12,16,45] and Number 16 as an input.

# Create a function  that takes list and number as an argument and return appropriate boolian and print

# Once done with the task, create a Pull Request on https://github.com/zelima/element-search

# Useful Example
    # for something in [1,2,3,4,5,6,7,8,98,9, 'hello']:
    #     print(something)

# for num in range(25):
#     print(num)
num = input('wich number R U lookin 4?\n')
mum = int(num)
list = [1,4,5,12,16,45]
#meore_naxevarshia = [len(list)/2]
#for num in [1,4,5,12,16,45]
a = 0
for num1 in [1,4,5,12,16,45]:
    if(num1 == mum):
        a = 1
if(a != 0):
    print('I found your Num!')
else:
    print('There is no Num.%s. in list!'%num)
