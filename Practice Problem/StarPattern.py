def first_star(n):
    print('First Star')
    for i in range(n+1):    
        print('* '*i)
        #for j in range(i):
        #print('*',end=' ')
        #print()

def inv_first_star(n):
    print("\nReverse of first star")
    ''' Reverse of first star'''
    print()
    for i in range(n+1):
        print("* "*(n-i))
        # or print(' * '*(n)) if range(n,0,-1)
        #for j in range(i):
        #print("*",end=' ')
        #print()


def second_star(n):
    print("\nSecond Star")
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end=' ')
        for j in range(i+1):
            print('*',end=' ')
        print()
def second_or(n):
    print('\nsecond star or')
    for i in range(n):
        print(' '*(n-i-1)+'* '*(i+1))

''' In second star func if we change print('*') to print(' * ') it show result of Equilateral trianlge func'''


def equi_tria(n):
    #print("\nEquilateral Triangle")
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end=' ')
        for j in range(i+1):
            print(' * ',end=' ')
        print()

def inv_equi_tria(n):
    #print('\ninverse Equilateral Triangle')
    for i in range(n,0,-1):
        for j in range(n-i):
            print(' ',end=' ')
        for j in range(i):
            print(' * ',end=' ')
        print()

def inv_third_or(n):
    for i in range(n,0,-1):
        print(''*n+'*'*i)


def diamond(n):
    for row in range(n):
        print(' '*(n-row-1)+'* '*(row+1))
    for col in range(n,0,-1):
        print(' '*(n-col)+'* '*col)


def hollow_triangle(n):
    for row in range(n):
        for col in range(n):
            if row==0 or col==n-1 or row==col:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
def hollow_diamond(n):
    for row in range(n+1):
        for col in range(n+1):
            if abs(row-col) == n//2 or row+col==n//2 or row+col==n+n//2+n%2:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

# def heart_shape(n):
#     for row in range(n):
#         for col in range(n+1):
#             if (col%(n//2)!=0 and row==0) or (row==1 and col%(n//2)==0) or (row-col==2) or(row+col==n+2):
#                 print('*',end=' ')
#             else:
#                 print(end=' ')
#         print()
# heart_shape(11)

def square_number(n):
    lst = [[0 for i in range(n)]for i in range(n)]
    l,h = 0,n-1
    num = 1
    c = (n+1)//2
    for i in range(c):
        for j in range(l,h+1):#h+1 will stop at h
            lst[i][j]=num
            num+=1
        for j in range(l+1,h+1):# becoz l is set to 5 by above loop 
            lst[j][h]=num
            num+=1
        for j in range(h-1,l-1,-1):
            lst[h][j] = num
            num+=1
        for j in range(h-1,l,-1):
            lst[j][l]=num
            num+=1
        l+=1
        h-=1    
    for i in range(n):
        for j in range(n):
            print(str(lst[i][j]).center(5,' '),end=' ')
        print()
    #print(lst)

def pascal_triangle(n):
    l = []
    for i in range(n):
        tl = []
        for j in range(i+1):
            if j==0 or j==i:
                tl.append(1)
            else:
                tl.append(l[i-1][j-1]+l[i-1][j])
        l.append(tl)
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end=' ')
        for j in range(i+1):
            print(f' {l[i][j]} ',end=' ')
        print()
