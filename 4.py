# -- coding: utf-8 --
# !/usr/bin/python3
# @Time    : 2021-03-18 23:22
# @Author  : 杜奕新
# @FileName: 4.py
# @Software: Pycharm Professional

f = open(r'D:\Git\Financial-Reporter-Analysis\t1.txt', 'r', encoding = 'utf8')
strings = f.read()
f.close()

ans = strings.split(' ')

all = []  # 全部去重
for i in ans:
	if i not in all:
		all.append(i)

count = {}  # 全部计数

for i in all:
	count.setdefault(i, 0)

for i in ans:  # 全部
	if i in list(count.keys()):
		count[i] = count[i] + 1

count = sorted(count.items(), key = lambda x:x[1], reverse = True)

for i in count:
	print(i)
