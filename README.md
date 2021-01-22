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

- The **import** statement can be used to import new modules and get access to new functions
    * `import <module_name>` -  But you have to use the function in the following way `module_name.function_name()`
    * `from <module_name> import function_name` - Then you can invoke the function without having to mention the module name just by `function_name()`

### User Defined Functions:

- Users can write their own functions in Python using the `def function_name()` statement and execute the function by just calling the `function_name()` where you want to execute it. 

- Users should consider defining functions where ever necessary where they are finding themselves using the same block of code again and again in order to prevent duplicating. 

- Functions also provide better readability, better run-time, and in-case you want to change what the code does, you just have to change it in the function rather than multiple lines of code.

- You can also pass parameters to your functions and such functions are called as **Parameterized Functions** and can accept arguments depending on the number of parameters the function accepts.

### Global and Local Scopes:

- A program can contain both **Global and Local Variables**. The variables that are declared and defined in the Global scope i.e. outside of any functions is called as a **Global Variable**, whereas the variables that are declared and defined within the local scope i.e. within a function is called as a **Local Variable**.

- The variable name inside a local scope can be same as the variable name in a global scope.

- The variables that are declared in the global scope can be accessed inside the functions i.e. local scope

- The variables that are declared in the local scope cannot be accessed outside in the global scope.

- The variables declared in one local scope cannot be accessed in another local scope.

- The global variables are declared and assigned a memory when the program starts and is de-allocated when the program ends

- The local variables are assigned a memory when the function is called and is de-allocated when the function ends.


## Error Handling:

- Errors can cause the program to crash

- A **divide-by-zero** error happens when you divide a number by Zero

- Errors can be handled within Python using the **try and except** statements.

- An error that happens inside a `try` block will cause code in the `except` block to execute

## Data Types in Python:

### Lists:

- A list is created by placing all the items inside square brackets `[]` separated by commas.
- It can have any number of items that belong to different datatypes like `int, float, String, etc`.
- A list can also have another list as an item within it called as the `nested list`.
- Similar to `Strings`, lists are also indexed and start with the index of 0.
- The value of a list can be acccessed in the follow way `list_name[index]`.
- The items inside a list can be deleted by `del list_name[index]`.












