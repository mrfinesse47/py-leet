# from https://www.youtube.com/watch?v=m3JgSV1Obn8&ab_channel=TechWithTim

from collections import deque

# pronounced deck

# a deque is faster to add elements to the beginning and end of a list

d = deque("hello")
print(d)
d.append('4')
d.append('5')
print("after appending")
print(d)
print("appending left")
d.appendleft("l")
print(d)
print("pop left")
d.popleft()
print(d)
print("to clear everything")
d.clear()
print(d)
print("you can exten a deque and place elements at the end")
d.extend("test")
d.extend([7, 8, 9])
print(d)
print("extend left places it in reverse")
d.extendleft("hey")
print(d)

print("to rotate the deque ")
d.rotate(-1)  # negative go left
print(d)

print("intilization with max length")

d = deque("hello", maxlen=5)
d.append("+")
print(d)
print("to access single element")
print(d[4])
