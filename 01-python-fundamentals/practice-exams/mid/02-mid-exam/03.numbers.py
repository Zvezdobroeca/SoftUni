nums = sorted([int(i) for i in input().split()], reverse=True)
avg = sum(nums) / len(nums)
result = [n for n in nums if n > avg][:5]

if len(nums) > 1 and result:
    print(*result)
else:
    print("No")
