# def recurssion_or_root(num):
#     def recurssion_wrapper(num, y=1, z=3):
#         if z == 0:
#             pass
#         return ((num/(num/y) +  yn)/2
from functools import reduce

marks = [('david', 80),('Tali',45),('moshe',86),('yanir', 80)]
fa = lambda x: reduce(lambda a,b: a and b, map(lambda i: i[1]>=55, x),True)
print(fa(marks[:1]+marks[2:]))
fb = lambda x: list(map(lambda z: z[0], filter(lambda y: y[1]<56, x)))
print(fb(marks))
fc = lambda x: min(map(lambda y: 100-y[1], x))