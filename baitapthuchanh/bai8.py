a,b,c = eval(input('nhap vao 3 so cach nhau boi dau phay:'))
if(a+b>c) and (a+c>b) and (b+c>a):
    if a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
        print('day la tam giac vuong')
    elif a==b==c:
        print('day la tam giac deu')
    elif a==b or a==c or b==c:
        print('day la tam giac can')
    else:
        print('day la tam giac thuong')
else:
    print('day Khong phai ba canh cua tam giac')