print("Water-Jug problem")
x=int(input("enter water quantity into 4 lit jug"))
y=int(input("enter water quantity into 3 lit jug"))
while True:
    rule_no=int(input("Enter rule number (1-8)"))
    if rule_no==1:
        if x<4:
            x=4
            print("(x,y) | (4,y)")
    if rule_no==2:
        if y<3:
            y=3
            print("(x,y) | (x,3)")
    if rule_no==3:
        if x>0:
            x=0
            print("(x,y) | (0,y)")
    if rule_no==4:
        if y>0:
            y=0
            print("(x,y) | (x,0)")
    if rule_no==5:
        if x+y>=4 and y>0:
            x,y=4,y-(4-x)
            print("(x,y) | (4,y-(4-x))")
    if rule_no==6:
        if x+y>=3 and x>0:
            x,y=x-(y-3),3
            print("(x,y) | (x-(y-3),3)")
    if rule_no==7:
        if x+y<=4 and y>0:
            x,y=x+y,0
            print("(x,y) | (x+y,0)")
    if rule_no==8:
        if x+y<=3 and x>0:
            x,y=0,x+y
            print("(x,y) | (0,x+y)")
    print("x=",x)
    print("y=",y)
    if x==2:
        print("goal state reached")
        break