"""
Scenario
Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.
Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - it's flat.
The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

Your task is to write a program which reads the number of blocks the builders have,
and outputs the height of the pyramid that can be built using these blocks.
Note: the height is measured by the number of fully completed layers -
if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.
"""
#I Method
blocks = int(input("Enter the number of blocks: "))


i = 1
no_of_blocks = 1
while no_of_blocks <= blocks:
    i+=1
    no_of_blocks = i*(i+1)/2

height = i-1

print("The height of the pyramid:", height)


# II Method
blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#
i = 1
no_of_blocks = 1
while no_of_blocks <= blocks:
    i+=1
    no_of_blocks = no_of_blocks+i

height = i-1

print("The height of the pyramid:", height)