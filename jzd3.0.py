#界址点检查程序 py3.8
#coding=utf-8
import os
import sys
import re
import tkinter as tk
from tkinter import filedialog

#通过re.split()方法，一次性拆分所有字符串
def go_split(s, symbol):
    # 拼接正则表达式
    symbol = "[" + symbol + "]+"
    # 一次性分割字符串
    result = re.split(symbol, s)
    # 去除空字符
    return [x for x in result if x]
#******************************************************
#检查单文件首末行数据错误及重复数据
def firsterror(files,path):
    for filename in files:
        if  os.path.splitext(filename)[1]==".txt":
            f=open(path+'\\'+filename,'r')
            lines=f.readlines()
            if lines is None or len(lines) ==0 :
               break
            if lines[0].strip('\n') != lines[(len(lines)-1)]: #比较首末行
               out.write('%s首末行数据错误(检查文件最后是否有空行)\n'%filename)
            if len(lines)!=len(set(lines)):
               out.write('%s有重复数据\n'%filename)
#******************************************************
#文件数组处理
def datacl(files,path):
    for filename in files: 
        line_num = 1
        if  os.path.splitext(filename)[1]==".txt":
            f=open(path+'\\'+filename,'r')
            total_line = len(open(path+'\\'+filename).readlines()) 
            while line_num <= total_line: 
                line=f.readline()
                line=line.strip()
                if line is None or len(line) ==0 :
                    break
                else:
                    data.append(filename+','+line)
    
    for i in range(0,len(data)):
        data[i]= go_split(data[i],symbol)
#******************************************************
#检查文件点号相同坐标不同错误出现
def secenderror(data):
    for  i in range(len(data)):
        for  j in range(len(data)):
            if i != j:
                if  data[i][1] == data[j][1]:
                    if data[i][2]!=data[j][2]or data[i][3]!=data[j][3]:
                        out.write('%s中%s与%s中%s有点号相同坐标不同错误出现\n'%(data[i][0],data[i][1],data[j][0],data[j][1]))
#******************************************************
#有坐标相同界址点号不同错误出现
def threeerror(data):
    for  i in range(len(data)):
        for  j in range(len(data)):
            if i != j:
                if data[i][1]!=data[j][1]:
                    if data[i][2]==data[j][2]:
                         if data[i][3]==data[j][3]:
                             out.write('%s中%s与%s中%s有坐标相同界址点号不同错误出现\n'%(data[i][0],data[i][1],data[j][0],data[j][1]))
#******************************************************
#主程序
#初始化参数
data=[]
symbol=','

# 打开选择文件夹对话框
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()
files = os.listdir(path)

out=open('界址点检查结果.txt','w')
out.write('检查%s下文件\n'%path)

firsterror(files,path)

datacl(files,path)

secenderror(data)

threeerror(data)

out.close()