'''
PE(M&D)(A&S)
### Parentheses  小括号() 一级优先
### Exponents    幂运算** 二级优先
### Multiplication & Division 乘除并列三级优先
### Addition & Subtraction 加减并列四级优先

+ plus

- minus

/ slash

* asterisk

% percent

< less-than

> greater-than

<= less-than-equal

>= greater-than-equal

'''

print('I will now count my chickens:')

print('Hens', 25.0 + 30 /6)
print('Roosters', 100.0 - 25 * 3 % 4)

print('Now I will count the eggs:')

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print('Is it true that 3 + 2 < 5 - 7?')

print(3 + 2 < 5 -7)

print('what is 3 + 2?', 3 + 2)
print('what is 5 - 7', 5 -7)

print('oh, that\'s why it\'s False.')

print('How about some more.')

print('Is it greater?', 5 > -2)
print('Is it greater or equal?', 5 >= -2)
print('Is it less or equal?', 5 <= -2)