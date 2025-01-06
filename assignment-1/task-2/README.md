# Difference between Python2 and Python3

### Print Function

In python2.x we use print as a statement rather than a function. We do not use pair of parenthesis to call the print function. Whereas in python3.x we use the pair of parenthesis to call the print function. It is an inbuilt function.

Python2.x
```
print 'Hello World!'
```

Python3.x
```
print("Hello World!")
```

This gives us the flexibility to provide args to the print function for using custom separators other than spaces, stream output into files easily and also designed to change the builtin property by using builtin.print .


```
def a():
    print()

__builtins__.print = a

print()
```

This will loop forever as we changed the function a to call whenever a call to print() is made.

### Integer Division 

In python2.x , the division operator returns integer when both operands are integers.But in python3.x, the division operator will always return integer irrespective of the operand data type.

Python2.x
```
>>> 7/2 
3
```

Python3.x
```
>>> 7/2
3.5
```

This gives the clarity that division operator will always return float and floor division operator will always return integer.

### Input Function 

Python2.x provides two functions to get input from the user namely `raw_input` and `input`.  
The `raw_input` function returns the input as a string data type while `input` function coverts the value into appropriate data type and returns the value.  
In python3.x, the `input` function gets the input from the user as a string data type and `raw_input` does not exist.

Python2.x
```
user_input = raw_input() # 7
type(user_input) # str
num = input() # 8
type(num) # int
```

Python3.x
```
val = input() #23
type(val) #str
```

### Round Function 

Round function always return float value in python2.x whereas in python3.x it will return with n digit precision and default it will return int data type.

### List Comprehension

In python2.x, list comprehension does not provide namespace resulting in value changes.But in python3.x there is no namespace leak.

Python2.x
```
num = 7 
ls = [num for num in range(100)]
print num  # 99
```

Python3.x
```
num = 7
ls = [num for num in range(100)]
print(num) # 7
```

### Range Function

In python2.x, there are two functions named `xrange` and `range`. `xrange` is used when we need better memory management and it returns a generator object. `range` function returns list object.  
In python3.x, there is no `xrange` function. The `range` function will return generator object and improved its performance.

### ASCII , Unicode and Byte types

In python2.x , there is ascii type and unicode type but there is no byte type.  
In python3.x, there is unicode string but not a function and there is also byte type.

There are more syntactical changes made like list comprehension does need parenthesis for tuple, `as` keyword is required for exception handling and there is no `next` attribute for generator objects.

Python2.x
```
generator = (letter for letter in 'abcdefg') 
next(generator) 
generator.next() 
[item for item in 1, 2, 3, 4, 5] 
try: 
    Python2 
except NameError, error: 
    print error, "An error Occurred"
```

Python3.x
```
[item for item in (1, 2, 3, 4, 5)] 
generator = (letter for letter in 'abcdefg') 
next(generator) 
try: 
    Python3
except NameError as error: 
    print (error, "THE ERROR HAS OCCURRED !") 
```