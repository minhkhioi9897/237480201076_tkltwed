a, b, c = eval(input("Enter a, b, c:"))
if a > b:
    if a > c:
        if b > c:
            print(c, b, a)
        else:
            print(b, c, a)
    else:
        print(b, a, c)
else:
    print(a, b, c)