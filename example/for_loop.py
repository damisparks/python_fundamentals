# Sample 1 
my_list = [
    6, "Lisbon", "new york", 
    ["This is now", "Hello", 123],
    2, 3, 4]
for i in (my_list): 
    # i is the iterator 
    # my_list is the iterable. 
    # 6 is the first element and expected to be printed first. 
    print(i)

# Sample 2 
another_list = [1,2,3, ["this is a test"]]
for i in another_list:
    if type(i) is list:
        print(f'{i} found.')        
    else:
        print(f'No list in {another_list}')