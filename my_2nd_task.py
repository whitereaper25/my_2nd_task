from collections import *
sample = input()
sample_1 = OrderedDict()
for i in range(sample):
    item = raw_input().split()
    Price= int(item[-1])
    Name= " ".join(item[:-1])
    if sample_1.get(Name):                       
       sample_1[Name] += Price
    else:
       sample_1[Name] = Price
for i in sample_1.keys():
    print i, sample_1[i]
