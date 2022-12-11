# Solution 1 to find the numbers
# Iterate over the list twice adding numbers to match target value

'''
def twoSum(nums, target):
    for i, n in enumerate(nums):
        for j, o in enumerate(nums):
            if n + o == target:
                return (i, j)
'''

#Solution 2 to find the index of numbers
# Iterate over the list, and subtract a number from traget and find the number remainder in list

def twoSum(nums, target):
    #create a dictionary
    d = {}

    for i, j in enumerate(nums):
        # get reminder from target
        rem = target - j
        #use print to view the dictionary
        #print(d)
        if rem in d:
            return d[rem], i
        d[j] = i

nums = [1,9,11,-2,15,-7, 10]
target = 19
if twoSum(nums, target) == None:
    print("target not matched")
else:
    print("numbers index are: ",twoSum(nums, target))