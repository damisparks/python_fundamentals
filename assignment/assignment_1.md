# Assignment 1 

## Exercise 1 
> ### Variables

The Python interpreter has strict rules for variable names. 
Which of the following are legal Python names? If the name is not legal, state the reason : 
1. and
2. and
3. var
4. var1
5. 1var
6. my-name
7. your name
8. COLOR


## Exercise 2 
> ### Types
It is important that we know the type of the values stored in a variable so that we can use the correct operators (as we have already seen!). Python automatically infers the type from the value you assign to the variable. Write down the type of the values stored in each of the variables below. Pay special attention to punctuation: values are not always the type they seem!
1. a = False
2. b = 3.7
3. c = ’Alex’
4. d = 7
5. e = ’True’
6. f = 17
7. g = ’17’
8. h = True
9. i = ’3.14159’
>To verify your answers, you can use the interactive Python shell, but first try to do the exercise without help.
```python
>>> x = 100
>>> type(x)
<type ’int’>
>>>
```


## Exercise 3
> ### String Operations
String operators might be a little less intuitive than those on numbers. This exercise will give you a chance to practice those. Given the following variables:
```
look = 'Look at me!'
now = 'NOW'
```
What are the values of the following expressions? 
Try to guess on your own before using your interpreter (but feel free to use your interpreter once you get stuck).
1. look[:4]
2. look[-1]
3. look*2
4. look[:-1] + now + look[-1]
5. now[1]
6. now[4]
7. look*2 + look[:-1] + now + look[-1]
For more on strings, see: http://docs.python.org/release/2.6.6/library/stdtypes.html#string-methods

## Exercise 4
> ### List Operations
For the following, write the line(s) of code that will emit the given Output. For each problem there may be more than
one correct answer; just give one. [More on lists](http://docs.python.org/release/2.6.6/tutorial/datastructures.html)
```python 
1. >>> a_list = [3, 5, 6, 12] >>> YOUR CODE HERE
3
2. >>> a_list = [3, 5, 6, 12] >>> YOUR CODE HERE
12
3. >>> a_list = [3, 5, 6, 12] >>> YOUR CODE HERE
[5, 6, 12]
4. >>> a_list = [3, 5, 6, 12] >>> YOUR CODE HERE
3
5
6 12
5. >>> a_list = [3, 5, 6, 12] >>> YOUR CODE HERE
[12, 6, 5, 3]
6. >>> a_list = [3, 5, 6, 12] >>> YOUR CODE HERE
[9, 15, 18, 36]
7. >>> a_list = [3, 5, 6, 12] >>> YOUR CODE HERE
[False, False, True, True]
```

## References.
Please note that this assignment was adapted from the [MIT OpenCourseWare, Massachusetts Institute of Technology](https://ocw.mit.edu/index.htm) 