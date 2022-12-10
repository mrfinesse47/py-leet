import math

# use pass to not execute
pass

# multiple assignments

n, m = 0, "abc"

n, m, z = 0.125, "abc", False

# Increment

n = n+1
n += 1
# n++ wont work

# None is null

r = None

# if statements dont need parens or curly braces

n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n -= 1

# logic operators
# && is actually and
# || is or

n, m = 1, 2

# if you have multiline if statements you need to use parens

# while loops are similar

n = 0
while n < 5:
    n += 1
    print(n)

# for loops

for i in range(5):
    print(i)

for i in range(2, 5):
    print(i)

# if you want to loop in reverse

for i in range(5, 1, -1):  # means to decrement by 1 each time, could pass in other numbers as
    # well to decrement by more
    print(i)

# math

print(5/2)  # will give 2.5

# double slash rounds down

print(5//2)

# with negative numbers if you need to round towards 0
# cast to int first

print(int(-3/2))

# modding for negative numbers doesnt work

print(-10 % 3)  # gives 2

# if you have to you can use the math module

print(math.fmod(-10, 3))

# more math helpers

print(math.floor(3/2))

print(math.ceil(3/2))

print(math.sqrt(9))

print(math.pow(2, 3))

# to get min max use

float("inf")

float("-inf")

# arrays are called lists in python

arr = [1, 2, 3]
print(arr)

# can be used as a stack

arr.append(4)
arr.append(5)

# to join 2 arrays use extend

arr1 = [1, 2, 3, 4]
arr2 = [5, 6]

arr1.extend(arr2)  # [1, 2, 3, 4,5,6]

print(arr1)

print(arr)

arr.pop()
print(arr)

# to insert into list

arr.insert(1, 7)  # inserting is o(n)

print(arr)

# to initialize an array to a certain value

n = 5
arr = [1]*n

print(arr)

# you can index and array by using negative numbers to et the end

print(arr[-1])

# sublists ie slicing is the best feature

arr = [1, 2, 3, 4, 5]

print(arr[1:3])  # does not include index 3 just like a for loop

# unpacking or destructuring

a, b, c = [1, 2, 3]
print(a, b, c)

# looping

nums = [1, 2, 3]

# using index

for i in range(len(nums)):
    print(nums[i])

# without index

for num in nums:
    print(num)

# with index and value

for i, n in enumerate(nums):
    print(i, n)

# another way to go in reverse

for i in reversed(range(len(nums))):
    pass

# and another

for index in range(len(nums)-1, -1, -1):
    pass


# looping through multiple arrays at the same time
# by zipping


print("zipping>>>>>>>>>")

nums1 = [1, 2, 3]
nums2 = [6, 4, 5]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

# reverse

nums = [1, 2, 3]
nums.reverse()
print(nums)

# sorting

arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)

arr = ["Kevin", "Rex", "Natalie", "Robert"]
arr.sort()  # will sort alphabetically
print(arr)

# custom sort


# class Solution:
#     def largestNumber(self, nums):
#         nums = list(map(lambda n: str(n), nums))

#         def sortfx(s1, s2):
#             if int(s1+s2) > int(s2+s1):
#                 return -1  # reverse order on -1 so the lower comes second
#             elif int(s1+s2) < int(s2+s1):
#                 return 1  # normal order on 1
#             else:
#                 return 0

#         nums.sort(key=functools.cmp_to_key(sortfx))
#         nums = "".join(nums)
#         return "0" if int(nums) == 0 else nums


# USE cmp_to_key to compare 2 values

# for intervals
# intervals.sort(key=lambda x: x.start)
# arr.sort(key=lambda x: (x[0], x[1])) second x[1] is a tie breaker
# arr.sort(key=lambda x: (x[0], -x[1])) here larger comes first due to neg sign
print(arr)

# list comprehension
arr = [i+i for i in range(5)]

print(arr)  # 0-4

# strings are similar to arrays
s = "abc"
print(s[0:2])

# strings are immutable
# s[0] = "A" -- wont work
# any time you update a string its considered n time

# if you need ascii
print(ord("a"))  # --97

# joining strings from array
strings = ["ab", "cb", "ef"]
print("".join(strings))  # or you could put a space etc.

# hash sets
mySet = set()

mySet.add(1)
mySet.add(2)

# resSet.add((nums[i], nums[l], nums[r])) adding tuple to set

print(mySet)
print(len(mySet))
print(1 in mySet)  # to find if value exists in set... important

print(set([1, 3, 4, 5, 5]))

# sHash[s[r]] = 1 + sHash.get(s[r], 0) - get or set if undef

# can also do set comprehension

mySet = {i for i in range(5)}
print(mySet)

# hash map

myMap = {}
myMap["Rex"] = 88

# search for key

print("Rex" in myMap)

# to remove a key

myMap.pop("Rex")

print(myMap)  # is now empty

# dictionary comprehension // hash maps are called dictionaries in py

m = {i: 2*i for i in range(3)}
print(m)

# looping through maps

m = {"name": "Kevin", "age": 33}
for key in m:
    print(key, m[key])

# or just iterate the values

for val in m.values():
    print(val)

# or get both

for key, val in m.items():
    print(key, val)

# tuples can be used as a key for a hash

m = {(1, 2): 3, 3: 5}

m = set()
m.add((1, 2))
print(m)

# lists cannot be key so this wont work
# so that is why we use tuples

# m[[3, 4]] = 5

# functions


def outer(a, b):
    c = "c"

    def inner():
        return a+b+c  # the inner variables will have access
    return inner()

# tricks

# single line return if else
# return True if 'e' in word else False


def single_line_return():
    # the in keyword can even check in strings
    return True if 'e' in "test" else False


print(single_line_return())

# sum max min

arr = [1, 2, 3, 4, 5]

# you can get the sum of array or min max

min(arr)  # 1
max(arr)  # 5
sum(arr)  # 15

# to convert to hex use

print(hex(0)[2:4].upper())

# optional params
# if using a list be careful


def inorderTraversal(self, node, res=None):
    res = [] if res is None else res

# if the function gets called again it wont release the list from the previous call

# scope to access a var outside a function:

# def diameterOfBinaryTree(root):
#     maxD = 0

#     def max_depth(root):
#         nonlocal maxD
