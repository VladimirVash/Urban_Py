first = int(input())
second = int(input())
third = int(input())

set_ = {first, second, third}

if len(set_) == 1:
    print(3)
elif len(set_) == 2:
    print(2)
elif len(set_) == 3:
    print(0)
