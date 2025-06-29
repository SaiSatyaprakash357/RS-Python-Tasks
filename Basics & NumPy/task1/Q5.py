# 5. Can a set contain tuples that themselves contain mutable elements (like lists)?
#    If not, how can you modify such a tuple to make it hashable and storable in a set?
#    What happens if you try to create a set like this:
#    my_set = { (1, [2, 3]) } 

# No a set can't contain tuples that themselves contain mutable elements (like lists) 
# we can use a tuple inside the tuple instead of list to solve this

my_set = { (1, (2, 3)) } 