# 6. This loop runs infinitely. Why?
#    x = 1.0
#    while x != 1.5:
#       print(x)
#       x += 0.1

# It runs infinitely because of floating-point precision errors
# Decimal numbers like 0.1 can't be represented exactly in binary and the binary value is slightly larger

x = 1.0
i=0
while x != 1.5:
    print(x)
    x += 0.1
    i += 1

    if i==10 :
        break

# In 6th itteration the value of x becomes 1.5000000000000004 which isn't equal to 1.5 
# So the loop runs infinitely