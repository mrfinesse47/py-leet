# 735. Asteroid Collision

#  [5,10,-50,7,-6,1]

# use stack for both move left to right
# if stack for positive is 0 add neg to result

class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        res = []
        i = 0
        length = len(asteroids)
        while i < length:
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:  # asteroids[i] < 0
                while len(stack) > 0:
                    absAstr = abs(asteroids[i])
                    if stack[-1] > absAstr:
                        break
                    elif stack[-1] < absAstr:
                        stack.pop()
                    else:
                        stack.pop()
                        break
                else:
                    res.append(asteroids[i])
            i += 1
        res.extend(stack)
        return res


print(Solution().asteroidCollision([-5]))
