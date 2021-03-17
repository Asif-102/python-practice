# x = 'hello bob'
# try:
#     y = int(x)
# except:
#     y= -1
# print('first', y)

# a = '123'
# try:
#     b = int(a)
# except:
#     b=-1
# print('second',b)

num = input('Enter a number: ')

try:
    getNum = int(num)
except:
    getNum = -1
if getNum > 0:
    print('Nice work')
else:
    print('Not a number')