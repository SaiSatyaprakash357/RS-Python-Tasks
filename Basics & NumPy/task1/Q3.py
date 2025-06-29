# 3. What happens if you modify the loop variable inside a for loop?
for i in range(5):
    print(i)
    if i == 2:
        i += 1

# The loop variable i is automatically updated on each iteration by range(5). 
# Any changes made to i inside the loop body are temporary and don’t affect the loop's overall behavior.