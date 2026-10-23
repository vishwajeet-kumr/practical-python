# REFACTOR THIS — organise it with functions

nums = [4, 7, 2, 9, 1, 5, 8, 3, 6]

total = 0
for n in nums:
    total += n
avg = total / len(nums)

biggest = nums[0]
for n in nums:
    if n > biggest:
        biggest = n

evens = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)

print(f"Numbers : {nums}")
print(f"Average : {avg:.1f}")
print(f"Biggest : {biggest}")
print(f"Evens   : {evens}")