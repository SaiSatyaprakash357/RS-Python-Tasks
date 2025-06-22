#4. Suppose you have a list of tuples and a set. 
#   How would you find all tuples where the first element exists in the set?
#   Example:
tuples_list = [ (1, "a"), (2, "b"), (3, "c"), (1, "d") ]  
target_set = {1, 3} 

filtered_tuples = [t for t in tuples_list if t[0] in target_set]
print(filtered_tuples)