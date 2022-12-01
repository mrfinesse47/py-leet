def max_water_area_container(height):
    l, r = 0, len(height) - 1
    cur_lvl = 0
    max_area = 0
    while l < r:
        cur_lvl = min(height[l], height[r])
        max_area = max(max_area, (r-l) * cur_lvl)
        if height[l] > height[r]:
            r -= 1
        elif height[r] > height[l]:
            l += 1
        else:
            l += 1
            r -= 1

    return max_area


levels = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_water_area_container(levels))
