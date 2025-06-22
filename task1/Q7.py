# 7. Convert this loop into a single line using list comprehension:
#    squares = []
#    for i in range(10):
#        if i % 2 == 0:
#            squares.append(i ** 2)

squares = [i**2 for i in range(10) if i % 2 == 0]
print(squares)