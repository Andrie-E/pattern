# Print the given pattern
# 1
# 22
# 333
# 4444
# 55555

# Pseudocode

# indicate how many rows needed
rows = 5
# create a for loop for the pattern
for i in range(1, rows + 1):
    for _ in range(i):
        print(i, end=" ")
# print the result
    print()
