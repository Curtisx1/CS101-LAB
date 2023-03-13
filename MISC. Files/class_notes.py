# 4.8 prime numbers
'''def is_prime(value):
    for count in range(2,value):
        if value % count == 0:
            return False
        else:
            return True

#4.7.1
x = int(input('num1:'))
y = int(input('num1:'))

def largest(a,b):
    if a > b:
        large = a
    else:
        large = b
    return large
print(largest(x,y))

#split() only works with strings
text = input() #10,20,30,40
new = []
my_list = text.split(',') #'10','20',
#convert to int
for i in my_list:
    i = int(i)
    new.append(i)
print(new)


# 4.32 multiples in a list
def is_list_mult10(my_list):
    for i in my_list:
        if i % 10 != 0:
            return False
    return True


def is_list_no_mult10(my_list):
    for i in my_list:
        if i % 10 == 0:
            return False
    return True


num = int(input())
input_list = []

while len(input_list) < num:
    elem = int(input())
    input_list.append(elem)
print(input_list)

if(is_list_no_mult10(input_list)):
    print('all multiples of 10')
elif (is_list_no_mult10(input_list)):
    print('no multiples of 10')
else:
    print('Mixed values')

# 5.6

value = input('Enter a string:\n')
print()
nums = input('Enter a start, end speerated by a comma wg 1, -2:\n')
atart = int(nums[0])
new_list = nums.split(',')
for i in range(len(new_lis)):
    new_list[i] = int(new_list[i])
start = new_list[0]
end = new_list[1]
print(f'The value is : {start}')
print(f'The end value is : {end}')
print(f'The value of {value} [{start}:{end}] is \'[{value[start:end]}\'')

# 5.2

value = input('Enter any string\n')
print()
for i in rang(len(value)):
    print(i, value[i])
for i, v in enumerate(value):
    print(i, v)

i = -1
while i >= - len(value):
    print(i, value[i])
    i = i -1

# 5.15
def new_(text):
    list_split = text.split()
    words = ""
    for x in list_split:
        if x[0].isupper():
            words += x[0]+'.'
    return words

value = input()
print(new_(value))

# Files

my_file = open("file.txt") # Creates the file object
my_file.close() # Closes the file after use

# 8.5


def splice(a_list, b_list):
    new_list = []
    small = min(len(a_list), len(b_list))
    for i in range(small):
        new_list.append(a_list[i])
        new_list.append(b_list[i])
    if len(a_list) > len(b_list):
        new_list.extend(a_list[small:])
    if len(b_list) > len(a_list):
        new_list += b_list[len(a_list):]
    return new_list

a = [1, 2]
b = [5, 9, 8, 4]
print(splice(a, b))
lst1 = splice([1,2,6,7,8])
lst2 = splice([1,2], [5])
lst3 = splice([1,2], [5,9,8,10])
print(lst1)
print(lst2)
print(lst3)'''


class Employee():
    def __init__(self, w=0, h=0):
        self.wage = w
        self.hour = h


emp = Employee()
print