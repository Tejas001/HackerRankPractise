# ##################
# s = input('Enter a string: ')
# s = list(s)
# print(s)
# special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']
# s1 = ''
# for c in s:
#     if c.islower() or c in special_ch or c.isspace() or c.isnumeric():
#         s1 += c.upper()
#     elif c.isupper() or c in special_ch or c.isspace() or c.isnumeric():
#         s1 += c.lower()

# print(s1)

# ##################
# def split_join(line):
# c = input('Enter a sentence: ').split(' ')
# a = ''
# a = "-".join(c)
# print(a)

# ##################
# def print_full_name(first, last):
#     print(f'Hello {first} {last}! You just delved into python.')
# f = input('Enter First name: ')
# l = input('Enter Last name: ')

# print_full_name(f,l)

# ##################
# meal_cost = float(input().strip())
# tip_percent = int(input().strip())
# tax_percent = int(input().strip())
# def solve(meal_cost, tip_percent, tax_percent):
#     tip = (tip_percent/100) * meal_cost
#     tax = (tax_percent/100) * meal_cost
#     total_cost = meal_cost + tip + tax
#     total_cost = round(total_cost)
#     print(total_cost)

# ##################
# solve(meal_cost, tip_percent, tax_percent)
# n = int(input().strip())
# cnt = 1
# while cnt <= n:
#     s = input('Enter a string: ').strip()
#     e = ''
#     o = ''
#     for i in  range(0,len(s)):
#         if i%2==0:
#             e +=s[i]
#         else:
#             o += s[i]
#     print(e,o)
#     cnt += 1

# ##################
# arr = []
# n = int(input().strip())
# for i in range(n):
#     arr.append(int(input().strip()))
# print(" ".join(map(str, arr[::-1])))

# ##################
# d = {}
# cnt = 0
# n = int(input('Enter a number of entry: ').strip())
# while cnt < n:
#     k,v = str(input('Enter a name in lowercase 8 digit number: ').strip().lower()).split(' ')
#     if not k.islower() and len(v) < 8:
#         print('Enter valid name in lowercase and phone number should be length of 8')
#     else:
#         d[k] = int(v)
#     cnt += 1
# while True:
#     name = input('Enter name to be searched or press (q/Q) to quit ').strip().lower()
#     if name == 'q' or name == 'Q':
#         break
#     elif name in d:
#         print(name,'=',d[name],sep='')
#     else:
#         print('Not found')

# ##################
# def factorial(n):
#     a = 1
#     if n < 0:
#         print(0)
#     else:
#         for i in range(a,n+1):
#             a = i * a
#     return a

# print(factorial(3))

# ####################
# from itertools import count
# import re

# n = int(input().strip())
# a = format(n,'b')
# l = re.split('0+',a)
# print(len(max(l)))

# arr = []
# arr = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
# for _ in range(6):
#     arr.append(list(map(int, input().rstrip().split())))

# a b c 2 4 4
#   d     2
# e f g 1 2 4 sum(19)
# res = []
# for x in range(0, 4):
#     for y in range(0, 4):
#         a = sum(arr[x][y:y+3]) + arr[x+1][y+1]+sum(arr[x+2][y:y+3])
#         res.append(a)
# print(res)
# print(max(res))

# Given an integer, , print the following values for each integer  from  to :
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary

# from os import sep


# def print_formatted(number):
#     w=len(bin(number)[2:])
#     for num in range(1,number+1):
#         # print(num)
#         print(str(num).rjust(w,' '),str(oct(num)[2:]).rjust(w,' '),str(hex(num)[2:]).rjust(w,' '),str(bin(num)[2:]).rjust(w,' '),sep=' ')
        
# if __name__ == '__main__':
#     n = int(input().strip())
#     # print(n)
#     print_formatted(n)

# import string
# def print_rangoli(size):
#     alpha = string.ascii_lowercase
#     n = size
#     L = []
#     for i in range(n):
#         s = "-".join(alpha[i:n])
#         # print(s)
#         L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
#     print('\n'.join(L[:0:-1]+L))

# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)

# s = input().strip()
# l = s.split(' ')
# print(' '.join(word.capitalize() for word in l))


# def minion_game(string):
#     vow = "AEIOU"
#     slen = len(string)
#     tsub = int(slen * (slen + 1) / 2)
#     k = sum(slen - i for i in range(slen) if string[i] in vow)   
#     s = tsub - k

#     if s > k: print(f"Stuart {s}")
#     elif s < k: print(f"Kevin {k}")
#     else: print("Draw")
# if __name__ == '__main__':
#     s = input()
#     minion_game(s)

# string = 'TEJAS'
# vow = "AEIOU"
# slen = len(string)
# tsub = int(slen * (slen + 1) / 2)
# for i in range(slen):
#     if string[i] in vow:
#         print(slen - i) 

# s = 'AABCAAADA'
# k = 3
# create = len(s)/k
# cnt = 0
# # def merge_the_tools(string, k):
# for i in range(0,len(s),k):
#     sett = ''.join(sorted(set(s[i:i+k]), key=s[i:i+k].index))
#     print(sett)

# Enter your code here. Read input from STDIN. Print output to STDOUT
# a = eval(input())
# b = eval(input())
# result = eval('abs(a)+abs(b)')
# print(result)
# from __future__ import print_function
# eval(input())


# import math
# import os
# import random
# import re
# import sys
# nm = input().split()
# n = int(nm[0])
# m = int(nm[1])
# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input().rstrip().split())))

# k = int(input())
# print(arr)

# k=1
# col = 3
# row = 2
# arr = [[2, 4, 2], [1, 1, 1]]
# sorted_arr = sorted(arr,key=lambda x:x[k])
# for i in range(len(sorted_arr)):
#     print(' '.join(str(sorted_arr[i][j]) for j in range(len(sorted_arr[0]))))

# print(any([1>0,1==0,1<0]))
# print(all([1>0,1==0,1<0]))


# N,s = input(),input().split()
# print( all(int(i) >= 0 for i in s) and any(j == j[::-1] for j in s))


# Enter your code here. Read input from STDIN. Print output to STDOUT
# from cgi import test
# import imp
# from itertools import count
# from math import ceil
# import re

# from audioop import reverse
# from math import comb
# from numpy import product


# vow = 'aeiouAEIOU'
# cons = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
# m = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]', input(), flags=re.I)
# print(m)
# if m:
#     print(*m, sep="\n")
# else:
#     print(-1)


# import re
# s = input()
# k=input()
# pattern = re.compile(k)
# r = pattern.search(s)
# if not r:
#     print('(-1, -1')
# while r:
#     print(f'({r.start()}, {r.end()-1})')
#     r = pattern.search(s,r.start()+1)

# a = list(reversed(range(1,11)))
# a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# a.remove(2)
# print(a)

# while True:
#     expr = input('Enter an expression: ').strip()
#     print('Result - ',eval(expr),sep='\n')

# my_email = input('Enter email id: ').strip()
# app_generated_password = getpass('Enter your password: ')

# t = int(input().strip())
# for r in range(t):
#     (a,b) = map(int,input().split(' '))

#     ans = a+b
#     print(ans)

# Recursive
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(3))
# a, b = 2
# print(a is b) # True
# print(a == b) # True

# Generator
# def repeat(n,msg):
#     for _ in range(n):
#         yield msg
# r = repeat(5,"Hi")
# for i in r:
#     print(i)

# Kwargs
# def test_dict(**data):
#     for k,v in data.items():
#         print(k,'=',v)
# print(test_dict(a=1,b=2,c=3))

# Args
# def test_list(*data):
#     for i in data:
#         print(i)

# print(test_list(1,2,3,4))

# Map
# a = [1,2,3,4,5]
# squared = list(map(lambda x:x*2,a))
# print(squared)


# class Calculator():

#     @staticmethod
#     def power(n,p):
#         if (n < 0) or (p < 0):
#             raise Exception('n and p should be non-negative')
#         print( n**p)

# mycal = Calculator()
# T = int(input())
# for i in range(T):
#     n,p = map(int,input().split())
#     try:
#         ans = Calculator.power(n,p)
#     except Exception as e:
#         print(e)

# Bubble sort
# if __name__ == "__main__":
#     n = int(input().strip())

#     a = list(map(int,input().rstrip().split()))
#     numswaps = 0
#     for i in range(len(a)-1,0,-1):
#         for j in range(i):
#             print(a[j],':', a[j+1])
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#                 numswaps += 1
#     print(f'Array is sorted in {numswaps} swaps.')
#     print(f'First Element: {a[0]}')
#     print(f'Last Element: {a[len(a)-1]}')

# Abstract class
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

# class Calculator(AdvancedArithmetic):
#     def divisorSum(self, n):
#         sum = 0
#         for i in range(n,0,-1):
#             if n%i==0:
#                 sum += i
#         return sum

# n = int(input())
# my_calculator = Calculator()
# s = my_calculator.divisorSum(n)
# print("I implemented: " + type(my_calculator).__bases__[0].__name__)
# print(s)

# r_date = list(map(int,(input().rstrip().split())))
# d_date = list(map(int,(input().rstrip().split())))


# if (d_date[0] >= r_date[0]) and (d_date[1] >= r_date[1]) and (d_date[2] == r_date[2]):
#     print(0)
# elif (d_date[0] < r_date[0]) and (d_date[1] == r_date[1]) and (d_date[2] == r_date[2]):
#     print(15*(r_date[0] - d_date[0]))
# elif (d_date[1] < r_date[1]) and (d_date[2] == r_date[2]):
#     print(500*(r_date[1] - d_date[1]))
# else:
#     print(10000)

# rd, rm, ry = [int(x) for x in input().split(' ')]
# ed, em, ey = [int(x) for x in input().split(' ')]

# if (ry, rm, rd) <= (ey, em, ed):
#     print(0)
# elif (ry, rm) == (ey, em):
#     print(15 * (rd - ed))
# elif ry == ey:
#     print(500 * (rm - em))
# else:
#     print(10000)

# from functools import reduce
# import imp
# from itertools import *

# from prometheus_client import Counter

# a = list(map(int,input().rstrip().split()))
# b = list(map(int,input().rstrip().split()))

# p = product(a,b)
# for i in p:
#     print(i,end=' ')

# a = input().rstrip().upper().split()
# prm = permutations(a[0],int(a[1]))
# l = []
# for i in prm:
#     l.append(''.join(i))
# l.sort()
# for i in l:
#     print(str(i))

# s,v = input().rstrip().split()
# print(sorted(s),v)

# l = []
# for i in range(int(v)):
#     for j in combinations(sorted(s),i+1):
#         l.append("".join(j))

# l.sort()
# l.sort(key=len)
# for i in l:
#     print(i)

# from itertools import combinations_with_replacement
# s,v = input().rstrip().split()

# # for i in range(int(v)):
# l = []
# for j in combinations_with_replacement(sorted(s),int(v)):
#     l.append("".join(j))
# for i in l:
#     print(str(i))

# def factorial(n):
#     f = 1
#     if n == 0:
#         print(1)
#     else:
#         for i in range(1,n+1):
#             f *= i
#     return f

# n1 = factorial(6)
# n2 = factorial(3)
# n3 = factorial(6-3)
# print(n1,n2,n3)
# n = n1/n2*n3
# print(n)

# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

from collections import Counter
import enum

# x = int(input('Enter a num: ').strip())
# l = list(map(int,input().rstrip().split()))
# costing = 0
# shopitems=Counter(l)

# for i in range(int(input('Enter a num: ').strip())):
#     c,v = list(map(int,input().rstrip().split()))
#     if shopitems[c]:
#         costing += v
#         shopitems[c] -= 1            
# print(costing)

# c,v = map(int,input().rstrip().split())
# print(c,v)

weekdays = ['sun','mon','tue','wed','thu','fri','sat']
# def testgen(days):
#     for i in days:
#         yield i

# days = testgen(weekdays)
# print(next(days))
# print(next(days))

# s = " ".join(weekdays) # list to str
# print(tuple(weekdays))      # list to tuple
# print(set(weekdays))      # list to set

# print(Counter(weekdays))
# print(weekdays.count('mon'))
# print([[x,weekdays.count(x)] for x in set(weekdays)])

# print(sum(range(1,4)))

# names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
# names2 = names1
# names3 = names1[:]

# print(id(names1))
# print(id(names2))
# print(id(names3))

# names2[0] = 'Alice'
# names3[1] = 'Bob'

# sum = 0
# for ls in (names1, names2, names3):
#     # if ls[0] == 'Alice':
#     #     sum += 1
#     # if ls[1] == 'Bob':
#     #     sum += 10
#     print(ls)

# print(sum)

# Python Program to Calculate Average of Numbers
# l = list(map(int,input().rstrip().split()))
# s = sum(l)
# l = len(l)
# avg = s/l
# print(avg)

# sum = 0
# for i in range(len(l)):
#     sum += l[i]
# avg = sum/len(l)
# print(avg)

# n = int(input().strip())
# rev = 0

# while n>0:
#     dig = n%10
#     print(dig)
#     rev = rev*10+dig
#     print(rev)
#     n = n//10
#     print(n)
#     print('#################')
# print(rev)

# a = 1234
# print(sum(list(map(int,list(str(a))))))

# a = 12345
# print(str(a)[::-1])
# if str(a) == str(a)[::-1]:
#     print(f'{a} is palindrome')
# else:
#     print(f'Not a palindrome')

# n = int(input().strip())
# cnt = 0

# for i in range(len(str(n))):
#     cnt += 1
# print(cnt)

# n = list(map(int,(input().rstrip().split())))
# print(sorted(n)[-2])

# v = 'aeiou'
# s = 'Hello World'
# cnt=0
# for i in s:
#     if i in v:
#         cnt +=1
# print(cnt)

# a = input().strip().lower()
# b = input().strip().lower()

# c = sorted(list(set(a) & set(b)))
# print(c)

# n = int(input())
# arr = list(map(int, input().split()))

# def average(arr):
#     setsum = sum(set(arr))
#     setlen = len(set(arr))
#     res = setsum/setlen
#     return res
# result = average(arr)
# print(result)

# s1 = list(map(int,input().rstrip().split()))
# s2 = list(map(int,input().rstrip().split()))
# s1,s2 = set(s1),set(s2)
# # l = []
# l1 = s1.difference(s2)
# l2 =s2.difference(s1)
# l = l1.union(l2)
# print('\n'.join(sorted(l)))

# a = input().split()
# b = [int(i) for i in input().split()]
# c = set([int(i) for i in input().split()])
# d = set([int(i) for i in input().split()])
# cnt = 0
# for i in b:
#     if i in c:
#         cnt += 1
#     if i in d:
#         cnt -= 1
# print(cnt)

# def unique_names(names1, names2):
#     names1.extend(names2)
#     print(names1)
#     s = sorted(list(set(names1)))
#     return s

# if __name__ == "__main__":
#     names1 = ["Ava", "Emma", "Olivia"]
#     names2 = ["Olivia", "Sophia", "Emma"]
#     print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia

# from collections import defaultdict
# def group_by_owners(files):
#     v = defaultdict(list)

#     for key, value in sorted(files.items()):
#         v[value].append(key)
#     return dict(v)

# if __name__ == "__main__":    
#     files = {
#         'Input.txt': 'Randy',
#         'Code.py': 'Stan',
#         'Output.txt': 'Randy'
#     }   
#     print(group_by_owners(files))

# from collections import defaultdict
# d = defaultdict(list)

# a,b = map(int,input().rstrip().split())

# for i in range(1,a+1):
#     d[input().strip()].append(str(i))

# for j in range(b):
#     print(' '.join(d[input().strip()]) or -1)

# from collections import namedtuple
# n, Score = int(input()) , namedtuple('Score',input().split())
# scores = [Score(*input().split()).MARKS for i in range(n)]
# print("%.2f"% (sum(map(int,scores))/n))
# print(scores)

# l = [1,2,3,4,5]
# print(list(filter(lambda x:x%2==0,l)))
# print(list(map(lambda x:x+2,l)))
# print(reduce(lambda x1,x2:x1+x2,l))

# from collections import OrderedDict

# ordereddict = OrderedDict()

# n = int(input().strip())
# for i in range(n):
#     item,space,qty = input().rpartition(' ')
#     ordereddict[item] = ordereddict.get(item,0)+int(qty)
# for k,v in ordereddict.items():
#     print(k,v)

# print(ordereddict)
# l = []
# # n=
# # print(n)
# for i in range(int(input().strip())):
#     l.append(input().strip())
# print(len(set(l)))

# l=set()
# # n=
# # print(n)
# for i in range(int(input().strip())):
#     l.add(input().strip())
# print(len(l))

# n = int(input())
# s = set(map(int, input().split()))
# nc = int(input())
# cnt = 1
# while cnt <= nc:
#     ch = input().rstrip()
#     if 'remove' in ch:
#         s.remove(int(ch.split()[-1]))
#     elif 'pop' in ch:
#         s.pop()
#     elif 'discard' in ch:
#         s.discard(int(ch.split()[-1]))
#     cnt += 1

# print(sum(s))

# n = int(input())
# s = set(map(int,input().split()))
# for i in range(int(input().strip())):
#     eval('s.{0}({1})'.format(*input().split()+['']))

# print(sum(s))

# l = [1,2,3,4,5]
# for i,j in enumerate(l):
#     print(i,j)

l = [1,2,3,4]
l.insert(4,5)
l.append(6)
l.remove(6)

print(l)