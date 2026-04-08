from scipy.integrate import quad
import numpy as np

# a = ['a', 'b', 'c']
# n = [1, 2, 3]
# x = [a, n]
# y=a+n
# z=x+n
# print(z)
# print(z[1])
# print(y)
# print(x)

# x[0]

# # print(x[0][1])
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# print(users)

# print(list(range(0, 10, 12)))
#  [0, 3, 6, 9]
# print(list)



# def f1(x):
#     return x
# def f2(x):
#     return x**2

# def integrand(x):
#     return f1(x)*f2(x)

# ans,err=quad(integrand,0,1)
# print(ans)

# def ask_ok(prompt,retries=4,reminder="Please try again!"):
#     while True:
#         if prompt in {'y','ye','yes'}:
#             return True
#         if prompt in {'n','no','nop','nope'}:
#             return False
#         retries=retries-1
#         if retries<0:
#             raise ValueError("Invalid user response")
#         return reminder
    
# print(ask_ok("Do not ask again"))

# pairs=[(1,'one'),(2,'two'),(3,'three'),(4,'four')]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)

# numbers=[1,2,3,4]
# dictionary={}
# for n in numbers:
#     dictionary[n]=n**2

# print(dictionary)

numbers=[1,2,3,4]
dictionary={n:n**2 for n in numbers}
print(dictionary)

# even_dict={n:n**2 for n in numbers if n%2==0}
# print(even_dict)

