# my_set={1,2,3,4,5}
# print(type(my_set))

# my_set2=set([1,2,3,4,5])
# print(type(my_set2))

import array as arr
a=arr.array('d',[1,2,3,4,5])
# a.extend([3.4,5.2,3.6])
# a.insert(2,0.6)
# b=arr.array('d',[9.2,7.38])
# c=arr.array('d')
# c=a+b
# print(a.pop(2))
# print(a.remove(2))
# print(a)

# class Stack:
#     def __init__(self):
#         self.items=[]

#     def is_empty(self):
#         return self.items==[]
#     def push(self,data):
#         self.items.append(data)
#     def pop(self):
#         return self.items.pop()
#     def pri(self):
#         return self.items
    
# s=Stack()
# while True:
#     print("push")
#     print("pop")
#     print("quit")

#     do=input("What you like to do:").split()
#     operation=do[0].strip().lower()

#     if operation=='push':
#         s.push(int(do[1]))
#     elif operation=='pop':
#         if s.is_empty():
#             print("stack is Empty")
#         else:
#             print("popped value:",s.pop())
#     elif operation == 'print':
#         print(s.items)

#     elif operation=='quit':
#         break

from  collections import deque
q=deque()
q.append("code")
q.append("eat")
q.append("repeat")

print(q.pop())
print(q.pop())
print(q.pop())
print(q)