# 10. Given a list l = [10, 20, 30, 40, 50]
#     write a program that removes the middle element (or elements if the length is even).

def remove_middle(li) :
    mid = len(li)//2
    if len(li) % 2 != 0 :
        li.pop(mid)
    else :
        li.pop(mid-1)
        li.pop(mid-1)
    return li

l1 = [10, 20, 30, 40, 50]
print (remove_middle(l1))
l2 = [10, 20, 30, 40, 50, 60]
print (remove_middle(l2))