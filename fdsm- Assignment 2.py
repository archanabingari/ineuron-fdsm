#!/usr/bin/env python
# coding: utf-8
1. "True" and "False" are two values of Boolean data type
    They can be  written as:
    x=True
    y=False2.  The three different types of boolean operators are:
   i)Logical AND - This operator returns true if both operands are true otherwise it returns false as output.
   example:
   x=10
   y=11
   z=12
   result=(x<y) and (x<z)
   This expression evaluates to True as both conditions are True.
   ii)Logical OR - This operator returns true if atleast one of the operands is true otherwise it returns false.
   example:
   x=10
   y=11
   z=12
   result=(x<y) or (x>z)
   This expression evaluates True since first condition is True.
   iii)Logical NOT - This operator is unary operator that negates the value of the operand.
   example:
   x=10
   y=11
   result=not(x>y)
   This expression evaluates True because the conidition is False 
   3.Logical AND truth table:
  x    |y    |output
  False|False|False
  False|True |False
  True |False|False
  True |True |True
  Logical OR truth table:
  x    |y    |output
  False|false|false
  False|True|True
  True|False|True
  True|True|True
  Logical NOT truth table:
  x    |output
  False|True
  True|False4.
  (5 > 4) and (3 == 5)
   (5>4)evaluates to True
   (3==5)evaluates to False
   true and false evaluates to be False
   Therefore, the expression evaluates to False
 
  not (5> 4)
   This expression evaluates to False
  
  (5 > 4) or (3 == 5)
    (5>4)evaluates to True
    (3==5)evaluates to False
    true or false evaluates to be True
    Therefore, the expression evaluates to True
   
  not ((5 > 4) or (3 == 5))
      (5>4)evaluates to True
      (3==5)evaluates to False
     true or false evaluates to be True
    Therefore, the expression evaluates to False
  
  (True and True) and (True == False)
    (True and true)evaluates to True
    (True==False)evaluates to False
    Therefore,This expression evaluates to False
    
  (not False) or (not True)
   True or False evaluates to True5.The six comparison operators are - 
i)Equal to (==): This operator determines whether two operands are equal and outputs true or false depending on the result. 
For instance:
5 == 5 #  True
5 == 6 # False

ii)not equal to (!=): operator determines whether two operands are not equal and returns true if they are and false otherwise.
For instance:
5!=6 # True

iii)Greater than (>): This operator determines whether the left operand is larger than the right operand, returning true if it is and false if it is not.
For instance:
5 > 4 # True
5 > 6 #  False

iv)Less than (<): This operator determines whether the left operand is less than the right operand and returns true if it is, and false if it is not. 
For instance:
The evaluation of 5<4 is False.


v)Greater than or equal to (>=): This operator determines whether the left operand is greater than or equal to the right operand, and if it is, it returns true; otherwise, it returns false.
For instance:
5 >= 4 # True
5 >= 6 #  False 
5 >= 5 #  True

vi) less-than-or-equal-to operator (<=): determines whether the left operand is less-than-or-equal-to the right operand and returns true if it is, else it returns false. 
For instance:
4 <= 3 # False
3 <= 4 #True
6.
Equal to (==) Operator:

The equal to operator (==) is used for comparison.
It compares two values to check if they are equal.
It returns a Boolean value (true or false) based on the comparison result.
The equal to operator is used in conditions, such as if statements or while loops, to make decisions based on equality.
example:
  x=10
  y=8
  if(x==5)
    return 5
  return y 

Assignment (=) Operator:

The assignment operator (=) is used for assignment or storing values in variables.
It assigns the value on the right-hand side to the variable on the left-hand side.
It does not perform a comparison but rather updates the value of a variable.
example:
  x=10
  This assign the value 10 to x
Therefore, the equal to (==) operator is used for comparison between two values, while the assignment (=) operator is used to assign a value to a variable. You would use the equal to operator in conditions to check for equality and make decisions based on the result. On the other hand, the assignment operator is used when you want to store a value in a variable or update its value.7.
Block 1-
if spam == 10:
 print("eggs")
This outputs eggs if spam is equal to 10.However the initial value of spam is 0 so this will not be executed.

Block 2-
if spam > 5:
 print("bacon")
else:
 print("ham")
This gives output as "bacon" if spam is greater than  5 otherwise "ham" is printed.Since spam=0 so "ham" is printed.
Block 3-
print("spam")
print("spam")
This block contains two print statements that will always execute.
8.
spam =  # Assume a value is stored in spam variable
if spam==1:
 print("Hello")
elif spam==2:
 print("Howdy")
else:
 print("Greetings!")9.
If a program is stuck in an endless loop,and you want to interrupt it's execution then one can use the following key's-
Ctrl+C : This sends interrupt signal to the program,stopping it's execution.
Ctrl+Break : On some systems or terminals, this combination can be used to stop the execution of a program.
Ctrl+\ : This key combination is sometimes used as an alternative to Ctrl + C to send a quit signal to the program, terminating its execution.
Ctrl+F2 :In some IDEss, this stops the prrogram.
10.
break : Exits the loop entirely.
When you want to terminate the loop based on aa  condition this can be used.
example:-
 for i in range(5):
  if i==3:
    break
  print(i)
 The looop stops when i equals to 3
  output:-
  0
  1
  2
continue : skips the current iteration and moves to the next iteration of loop
example:-
 for i in range(5):
  if i==3:
   continue # skips iteration when i equals to 3
  print(i)
 output:-
 0
 1
 2
 4
11.
range(10): This form of the range function generates a sequence of numbers from 0 to 9 (10 numbers in total). It starts from the default initial value of 0 and increments by 1 for each subsequent number. The step size is implicitly set to 1.
example-
for i in range(10):
 print(i)
output:-
0
1
2
3
4
5
6
7
8
9

range(0, 10): This form of the range function specifies both the start and stop values explicitly. It generates a sequence of numbers from 0 to 9 (10 numbers in total). Similar to range(10), the step size is implicitly set to 1.
example-
for i in range(0,10):
 print(i)
output:-
0
1
2
3
4
5
6
7
8
9

range(0, 10, 1): This form of the range function includes both the start, stop, and step values. It generates a sequence of numbers starting from 0 and ending at 9 (10 numbers in total), with a step size of 1.range(0, 10, 1): This form of the range function includes both the start, stop, and step values. It generates a sequence of numbers starting from 0 and ending at 9 (10 numbers in total), with a step size of 1.
example-
for i in range(0,10,1):
 print(i)
output:-
0
1
2
3
4
5
6
7
8
912.
Using for loop -
for i in range(1,11):
    print(i)
 
Using while loop -
i=1
while i<=10:
 print(i)
 i+=113.
spam.bacon()