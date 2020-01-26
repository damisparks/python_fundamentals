a = 4 
b = 6 
c = 4
if a < b:
    print(f'{a} is  less than {b}')
if c == a: 
    # if true 'Hurray' will be printed,
    # if False, it goes into the elif below. 
    # Try changing the conditon to evaluate to false.
    print(f'Hurray')
elif type(a) is type(b):
    print(f'{a} and {b} are of the same type ')
else:
    print(f'{a} is not less than {b}')
