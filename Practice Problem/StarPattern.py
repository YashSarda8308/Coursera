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
first_star(5)
inv_first_star(5)

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
second_star(5)
second_or(5)
''' In second star func if we change print('*') to print(' * ') it show result of Equilateral trianlge func'''


def equi_tria(n):
    #print("\nEquilateral Triangle")
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end=' ')
        for j in range(i+1):
            print(' * ',end=' ')
        print()
equi_tria(5)
def inv_equi_tria(n):
    #print('\ninverse Equilateral Triangle')
    for i in range(n,0,-1):
        for j in range(n-i):
            print(' ',end=' ')
        for j in range(i):
            print(' * ',end=' ')
        print()
inv_equi_tria(5)
def inv_third_or(n):
    #print('\ninverse of third or')
    for i in range(n,0,-1):
        print(''*n+'*'*i)
inv_third_or(5)
def fourth_star(n):
    print()
    k = 2*n-1
    for i in range(n):
        for j in range(k):
            print("*"*(i-j),end=' ')
        print()

def diamond(n):
    for i in range(n):
        print(' '*(n-i-1)+'* '*(i+1))
    for j in range(n,0,-1):
        print(' '*(n-j)+'* '*j)
#def neat_diamond
diamond(5)