#界址点检查程序 py3.8 改写类
#coding=utf-8
import os
import sys
import re
class Jzd():
    def __init__(self,path,outfile):
        self.symbol=','
        self.path=path
        self.files = os.listdir(path)
        self.outfile=outfile
        self.out=open(outfile,'a+')
        self.data=[]
    #通过re.split()方法，一次性拆分所有字符串
    def go_split(self,s, symbol):

        # 拼接正则表达式
        symbol = "[" + symbol + "]+"
        # 一次性分割字符串
        result = re.split(symbol, s)
        # 去除空字符
        return [x for x in result if x]
    #******************************************************
    #检查单文件首末行数据错误及重复数据
    def firsterror(self,files,path):
        for filename in files:
            if  os.path.splitext(filename)[1]==".txt":
                f=open(path+'\\'+filename,'r')
                lines=f.readlines()
                if lines is None or len(lines) ==0 :
                   break
                if lines[0].strip('\n') != lines[(len(lines)-1)]: #比较首末行
                   self.out.write('%s首末行数据错误(检查文件最后是否有空行)\n'%filename)
                if len(lines)!=len(set(lines)):
                   self.out.write('%s有重复数据\n'%filename)
    #******************************************************
    #文件数组处理
    def datacl(self,files,path):
        for filename in files: 
            line_num = 0
            if  os.path.splitext(filename)[1]==".txt":
                f=open(path+'\\'+filename,'r')
                while True:
                    line=f.readline()
                    if line:
                        line=line.strip()
                        if len(line) :
                             self.data.append(filename+','+line)
                    else:
                        break
        for i in range(0,len(self.data)):
            self.data[i]= self.go_split(self.data[i],self.symbol)
    #******************************************************
    #检查文件点号相同坐标不同错误出现
    def secenderror(self,*data):
        for  i in range(len(self.data)):
            for  j in range(len(self.data)):
                if i != j:
                    # print(data)
                    # print(len(data))
                    # print(data[0][1][1])
                    # print(j)
                    # print(data[j][1])
                    if  data[0][i][1] == data[0][j][1]:
                        if data[0][i][2]!=data[0][j][2]or data[0][i][3]!=data[0][j][3]:
                            self.out.write('%s中%s与%s中%s有点号相同坐标不同错误出现\n'%(data[0][i][0],data[0][i][1],data[0][j][0],data[0][j][1]))
    #******************************************************
    #有坐标相同界址点号不同错误出现
    def threeerror(self,*data):
        for  i in range(len(self.data)):
            for  j in range(len(self.data)):
                if i != j:
                    if data[0][i][1]!=data[0][j][1]:
                        if data[0][i][2]==data[0][j][2]:
                             if data[0][i][3]==data[0][j][3]:
                                 self.out.write('%s中%s与%s中%s有坐标相同界址点号不同错误出现\n'%(data[0][i][0],data[0][i][1],data[0][j][0],data[0][j][1]))
    #******************************************************
    def run(self):
        out=open(self.outfile,'w')
        # out=open('界址点检查结果4.txt','w')
        out.write('检查%s下文件\n'%self.path)
        self.firsterror(self.files,self.path)
        self.datacl(self.files,self.path)
        self.secenderror(self.data)
        self.threeerror(self.data)
        out.close()