# Python-Training
This repository contains some sample Python codes from the Automate-the-Boring-Stuff-with-Python Udemy Training

---
## Basic Terminology and using IDLE 

- <b> Expression </b> - Every expression constitutes of values and operators, e.g. ( 2 + 5) and the expression evaluates to give us another single value.
- <b> Operators </b> - Any operation that must be performed on a given value are called as operators. Some of the operators that are supported in Python are as listed below.

     * Arithmetic operators (+ - * / // % ** )
     * Assignment operators (=)
     * Comparison operators (==, <, >, <=, >=, !=)
     * Logical operators (and or not)
     * Identity operators (is, is not)
     * Membership operators (in, not in)
     * Bitwise operators (&, |, ~ ^).

     
> <b>Note:</b> The operators are calculated in the order of precedency where Multiplication and Division are operated first and then Addition and Subtraction. 

- <b> Data Type </b> - Every value that is written in the Python programming language has an Data Type associated with it. The most common types of Data Types are as listed below:

	* String - str
	* Numeric - int, float
	* Sequence - list, tuples, range
	* Mapping - dict
	* Set - set
	* Boolean - bool 
 
- <b> Variables </b> - You can store the values in memory by using variables and you can assign the values to these variables using the assignment operator (=). 


## Boolean Expressions and Operators:

- **Boolean Expressions** - Boolean Expressions can contain either 'True' or 'False'.
- **Boolean Operators** - Boolean Operators are expressions that can evaluate to a Boolean Value i.e. 'True' or 'False'. The Boolean Operators or the Logical Operators are **And, Or and Not**

### The 'OR' operator Truth Table:

| Expression | Evaluates to  |
|--|--|
| True or True | True  |
|True or False | True |
|False or True| True|
|False or False| False|

### The 'AND' operator Truth Table:

| Expression | Evaluates to  |
|--|--|
|True and True | True|
|True and False | False|
|False and True | False|
|False and False| False|

### The 'NOT' operator Truth Table:

| Expression | Evaluates to  |
|--|--|
|not True | False  |
|not False | True |

## Conditional Statements:

### if, else and elif Statements:

- **if Statement** - The **'if'** statement is used to check if the variable matches a particular value or not. If the expression evaluates to **'True'** then the block of code under the **'if'** statement is executed. 

- **else Statement** - The **else** statement is used if you want to have more than one condition to be checked. If the expression evaluates to **'True'** then the block of code under the **'if'** statement is executed. Otherwise the block of code under the **'else'** statement is executed. 

- **elif Statement** - The **elif** statement is used when you need to have multiple i.e. more than two conditions to be checked. The block of code that evaluates to **'True'** is executed.

### While Loops:

- **While Loops** - The **'While'** loops statements are used when you want to run a block of code for a specified number of times or if you want to run a block of code until the condition of the statement evaluates to **'False'**. The **'While'** loop statements are **'Entry Check Loops'** meaning that the condition is checked before entering the loop and exits when the condition is not satisfied. i.e. The Loop will not run even once if the condition is not satisfied.

    * **Break Statements** -  The **Break Statements** are used when you want to exit/break a block of code and resumes execution at the next statement
    * **Continue Statement** - The **Continue Statements** are used when you want to return the control to the beginning of the while loop. The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop. The continue statement can be used in both while and for loops.

### For Loops:

- **For Loops** - The **For** loops can be used when you know how many number of times you want to run the loop. The **While** loop can be used to achieve the same results, but the **For** loop is the most defined way to code when you know how many times you want to run the loop.

## Functions in Python:

### Built-in Functions:

- Python has a large number of Built-in functions that can support the users to achieve the most commonly used or the perform the common tasks. The functionalities of these Built-in functions are pre-defined and can be used to perform several functions. Some of the commonly used Built-in functions are **print(), int(), len(), abs(), append() etc.**














