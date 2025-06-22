# 11. Without using slicing ([::-1]) or the reverse() method, 
#     reverse the list l = [5, 6, 7, 8, 9] using a loop or logic.

l = [5, 6, 7, 8, 9]
length = len(l)
for i in range(length//2) :
    l[i], l[length-1-i] = l[length-1-i], l[i]

print(l)