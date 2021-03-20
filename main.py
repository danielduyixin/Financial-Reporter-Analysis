# -- coding: utf-8 --
# !/usr/bin/python3
# @Time    : 2021-03-18 20:27
# @Author  : 杜奕新
# @FileName: main.py
# @Software: Pycharm Professional

from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_page


def read_pdf(pdf):
	# resource manager
	rsrcmgr = PDFResourceManager()
	retstr = StringIO()
	laparams = LAParams()
	# device
	device = TextConverter(rsrcmgr, retstr, laparams = laparams)
	process_page(rsrcmgr, device, pdf)
	device.close()
	content = retstr.getvalue()
	retstr.close()
	# 获取所有行
	lines = str(content).split("\n")
	return lines


if __name__ == '__main__':
	with open(r'D:\Git\Financial-Reporter-Analysis\年报\ST景谷2019.pdf', "rb") as my_pdf:
		print(read_pdf(my_pdf))
