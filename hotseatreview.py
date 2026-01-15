def x(nums):
    biggest = nums[0] # 90
    for n in nums:
        if n > biggest:
            biggest = n
    print(biggest)

grades = [90, 77, 70, 99, 68, 69, 100]

x(grades)