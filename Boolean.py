x = bool ()
y = bool ()

print ('Enter x as 1 or 0:')
x = int (input())

print ('Enter y as 1 or 0:')
y = int (input())

z = str(not bool(x and y))

print ('The Boolean value of x is', str(bool (x)))
print ('The Boolean value of y is', str(bool (y)))
print ('The Boolean value of (x and y) is', str(bool (x and y)))
print ('The Boolean value of (x not y) is', z)
