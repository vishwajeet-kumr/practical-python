# calculate_average(), 
# find_maximum(), 
# find_evens(), 
# print_summary(), and 
# main() — with if __name__ == '__main__': main()
nums = [4, 7, 2, 9, 1, 5, 8, 3, 6]

def calculate_average(nums):
    '''Returns the avg marks''' 
    return sum(s for s in nums)/len(nums)

def find_maximum(nums):
    return max(nums)

def find_evens(nums):
    evens = []
    for s in nums:
        if s % 2 == 0:
            evens.append(s)
    return evens

def print_summary(nums):
    Num = nums
    avg = calculate_average(nums)
    biggest = find_maximum(nums)
    even = find_evens(nums)

    print(f"\n{'------------ SUMMARY ------------'}")
    print(f"Numbers   : {Num}")
    print(f"Average   : {avg:.2f}")
    print(f"Biggest   : {biggest}")
    print(f"Evens     : {even}")

if __name__ == '__main__':
    print_summary(nums)
    

