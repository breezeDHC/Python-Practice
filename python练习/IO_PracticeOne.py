#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
import os,time
dir = '/home/dhc/桌面/dhc/python练习'
def dir_L():
    li = os.listdir(dir)
    print('mode\tnlike\tfilenum\tuser_id\tgroup_id\tsize\tmonth\tday\ttime\tfilename\t')
    for n in li:
        attrTuple = os.stat(n)
        print(str(attrTuple.st_mode)+'\t',end='')
        print(str(attrTuple.st_nlink)+'\t',end='')
        fileNum = file_num(dir,n)
        print(str(fileNum)+'\t',end='')
        print(str(attrTuple.st_uid)+'\t',end='')
        print(str(attrTuple.st_gid)+'\t\t',end='')
        print(str(attrTuple.st_size//1024)+'K\t',end='')
        timeTuple = time.localtime(attrTuple.st_mtime)
        print(str(timeTuple.tm_mon)+'月\t',end='')
        print(str(timeTuple.tm_mday)+'\t',end='')
        print(str(timeTuple.tm_hour)+':'+str(timeTuple.tm_min)+'\t',end='')
        print(n+'\t')
#计算某个路径的文件数，若该路径是一个文件或者一个空文件夹则为1
def file_num(di,n):
    sub_path = os.path.join(di,n)
    if os.path.isfile(sub_path):
        return 1
    else:
        fileNum = 0
        if os.path.isdir(sub_path):
            subli = os.listdir(sub_path)
            for x in subli:
                if os.path.isfile(x):
                    fileNum = fileNum + 1
                else:
                    fileNum = fileNum + file_num(sub_path,x)
        return fileNum
    
dir_L()

