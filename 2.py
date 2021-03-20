# -- coding: utf-8 --
# !/usr/bin/python3
# @Time    : 2021-03-18 20:43
# @Author  : 杜奕新
# @FileName: 2.py
# @Software: Pycharm Professional
import jieba

strings = open('text.txt', 'r', encoding = 'utf8').read()
result = jieba.lcut(strings)
dois = ['，', '。', '、', '？', '！', '’', '‘', '（', '）', '“', '”', ',', '/', '：', '；']

ans = []  # 全部去除标点符号
for i in result:
	if i not in dois:
		ans.append(i)

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
	# print(f'{i[0]}:{i[1]}')
	print(i)
