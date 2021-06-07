n=True
while n==True:
    print("hello I am calculator")
    print("NOTE--DO NOT FEED ANY TYPE OF SYMBOL OR UNIT DURING CALCULATION,FEED ONLY NUMBERS")
    print("area and perimeter--------------------------1")
    print("square,cube,square root and cube root-------2")
    print("simple interest-----------------------------3")
    print("exponent------------------------------------4")
    print("table of any number-------------------------5")
    print("percentage----------------------------------6")
    print("profit-loss---------------------------------7")
    print("discount------------------------------------8")

    x=input("enter the number given in front of the function which you want to do").lower()
    if x=='1' :
        print("area of rectangle---------------------------a")
        print("perimeter of rectangle----------------------b")
        print("area of square------------------------------c")
        print("perimeter of square-------------------------d")
        print("circumference of circle---------------------e")
        print("area of circle------------------------------f")
        y=input("enter the letter given in front of the function which you want to do")
        if y=='a':
                g=int(input("enter the length of the rectangle"))
                h=int (input("enter the breadth of the rectangle"))
                cd=g*h
                print("area of the rectangle is:",cd)
        elif y=='b':
                a=int(input("enter the length of the rectangle"))
                b=int(input("enter the breadth of the rectangle"))
                print("perimeter of the rectangle= 2(l+b),so perimeter=",2*(a+b))
        elif y=='c':
                a=int(input("enter the measure of side"))
                print("area of square=side*side,so area=",a**2)
        elif y=='d':
                a=int(input("enter the measure of length of side of square"))
                print("perimeter of square=4*side,so perimeter=",4*a)
        elif y=='e':
                a=int(input("enter the radius of the circle"))
                print("circumference of the circle=2*pie*radius,so circumference=",2*22/7*a)
        elif y=='f' :
                a=int(input("enter the radius of the circle"))
                print("area of circle=pie*radius*radius,so area=",22/7*a*a)
        else:
            print("wrong input")
    elif x=='2':
        print("square of a number-------------------------a")
        print("cube of a number---------------------------b")
        y=input("enter the letter given in front of the function which you want to do")
        if y=='a':
                c=int(input("enter the number of which you want to find square"))
                print("square of the number=",c*c)
        elif y=='b':
                d=int(input("enter the number of which you want to find cube"))
                print("cube of the number=",d*d*d)
        else:
            print("wrong input")
    elif x=='3':
        print("simple interest----------------------------a")
        print("amount of simple interest------------------b")
        print("principal on a simple interest-------------c")
        print("rate on a simple interest------------------d")
        print("time on a simple interst-------------------e")
        y=input("enter the letter given in front of the function which you want to do")
        if y=='a':
                f=int(input("enter the principal amount"))
                g=float(input("enter the rate"))
                h=int(input("enter the time"))
                print("simple interest=",(f*g*h)/100)
        elif y=='b':
                f=int(input("enter the simple interest"))
                g=int(input("enter the principal amount"))
                print("amount=",f+g)
        elif y=='c':
                f=int(input("enter the simple interest"))
                g=int(input("enter the rate"))
                h=int(input("enter the time"))
                print("principal amount=",(f*100)/(g*h))

        elif y=='d':
                f=int(input("enter the simple interest"))
                g=int(input("enter the principal"))
                h=int(input("enter the time"))
                print("rate =",(f*100)/(g*h))
        elif y=='e':
                f=int(input("enter the simple interest"))
                g=int(input("enter the principal"))
                h=int(input("enter the rate"))
                print("time=",(f*100)/(g*h))
        else:
            print("wrong input")
    elif x=='4':
        print("value of an exponent------------------------a")
        y=input("enter the letter given in front of the function which you want to do")
        if y=='a':
                f=int(input("enter the base number"))
                g=int(input("enter the power of the number"))
                print("The value of the exponent=",f**g)
        else:
            print("wrong input")
    elif x=='5':
                b=int(input("enter a number"))
                print("Table of",b)
                print(b*1,b*2,b*3,b*4,b*5,b*6,b*7,b*8,b*9,b*10)
    elif x=='6':
        print("convert fraction into percent------------------------------------------------------------a")
        print("To find 'x'% of 'y'----------------------------------------------------------------------b")
        print("the percent of one quantity'x' to other quantity'y'--------------------------------------c")
        y=input("enter the letter given in front of the function which you want to do")
        
        if y=='a':
            x=int(input("enter the numerator of fraction"))
            y=int(input("enter the denominator of the fraction"))
            print("the fraction in percentage=",(x*100)/y)

        elif y=='b':
            x=int(input("enter how much percentage you want to find"))
            z=int(input("enter the quantity of which you want to find the given percentage"))
            g=100
            print("The answer is",(x*z)/g)

        elif y=='c':
            x=int(input("enter the first quantity 'x'"))
            z=int(input("enter the second quantity 'y'"))
            print("The required percentage=",(x*100)/z)
        else:
            print("wrong input")

    elif x=='7':
            print("to find profit--------------------------a")
            print("to find loss----------------------------b")
            print("to find gain%---------------------------c")
            print("to find loss%---------------------------d")
            print("to find selling price if there is gain--e")
            print("to find selling price if there is loss--f")
            print("to find cost price if their is gain-----g")
            print("to find cost price if their is loss-----h")
            y=input("enter the letter given in front of the function which you want to do")
            if y=='a':
                    x=int(input("enter the selling price"))
                    z=int(input("enter the cost price"))
                    print("total gain=",x-z)
            elif y=='b':
                    x=int(input("enter the selling price"))
                    z=int(input("enter the cost price"))
                    print("total loss=",z-x)
            elif y=='c':
                    x=int(input("enter the selling price"))
                    z=int(input("enter the cost price"))
                    g=100
                    print("gain%=",(x-z)/z*g)
            elif y=='d':
                    x=int(input("enter the selling price"))
                    z=int(input("enter the cost price"))
                    g=100
                    print("loss%=",(z-x)/z*g)
            elif y=='e':
                    x=int(input("enter the gain%"))
                    z=int(input("enter the cost price"))
                    g=100
                    print("selling price=",(g+x)/100*z)
            elif y=='f':
                    x=int(input("enter the loss%"))
                    z=int(input("enter the cost price"))
                    g=100
                    print("selling price=",(g-x)/100*z)
            elif y=='g':
                    x=int(input("enter the gain%"))
                    z=int(input("enter the selling price"))
                    g=100
                    print("cost price=",100/(g+x)*z)
            elif y=='h':
                    x=int(input("enter the loss%"))
                    z=int(input("enter the selling price"))
                    g=100
                    print("cost price=",100/(g-x)*z)
            else:
                    print("wrong input")

    elif x=='8':
            print("to calculate discount-------------------------------------------------a")
            print("to calculate discount%------------------------------------------------b")
            print("to find selling price-------------------------------------------------c")
            print("to find marked price--------------------------------------------------d")
            y=input("enter the letter given in front of the function which you want to do")
            if y=='a':
                    x=int(input("enter the marked price"))
                    z=int(input("enter the selling price"))
                    print("discount=",x-z)
            elif y=='b':
                    p=int(input("enter the marked price"))
                    q=int(input("enter the selling price"))
                    g=100
                    print("discount%=",(p-q)/p*g)    
            elif y=='c':
                    p=int(input("enter the rate of discount"))
                    q=int(input("enter the marked price"))
                    g=100
                    print("Selling price=",(g-p)/g*q)
            elif y=='d':
                    p=int(input("enter the rate of discount"))
                    q=int(input("enter the selling price"))
                    g=100
                    print("marked price=",(q*g)/g-p)


    else:
        print("wrong input")



    result=input("Do you want to repeat the program:yes / no").lower()
    if result=="yes":
        continue
    else:
        exit()
