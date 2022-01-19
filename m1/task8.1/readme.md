# Module 8 Python Essentials

## Task 8.1

I've created a script for resolve a quadratic equations on demands described in the task. I tested it out for three cases: 
 - equation has two roots:
 
![resolving an equation with two roots](./images/1.png?raw=true)

 - equation has one root:
 
![resolving an equation with one root](./images/2.png?raw=true)

 - equation has no roots:
 
![resolving an equation with no roots](./images/3.png?raw=true)

The program can be run without arguments as well, so I can define them while running it:

![resolving an equation with sequential argument passing](./images/4.png?raw=true)

It has three attempts to set the parameter:

![setting parameter with invalid data](./images/5.png?raw=true)

And if I mistype a parameter three times after that the program decides that I got tired and will wait for me next time. It works with arguments passing way too:

![setting parameter with invalid data through arguments](./images/6.png?raw=true)

Then I wrote three unit tests for `discriminant`, `roots` and `solv_square` functions and launched it:

![running unit tests](./images/7.png?raw=true)

In the end, I've tested exit codes from my script. I created two cases: in the first the script ends without errors, showed the result and returned the code '0' which is 'OK', but in the second case the script ends with error, that matches with code '1':

![testing exit codes in two cases](./images/8.png?raw=true)

