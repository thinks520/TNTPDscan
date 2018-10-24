#!/usr/bin/python
#coding:utf-8

import sys
from help import *

if __name__ == "__main__":

    helps = '''
    ************声明*************
    本工具仅限安全研究使用，使用者严禁恶意使用扫描，后果自行负责！！！！

            ----by：黑客小平哥（如有任何改进建议请发送邮箱：1241144977@qq.com）

    *********************************************************************************

            -u                          指定URL扫描

            -us                         获取urls.txt文件中URL进行批量扫描

            -p                          指定端口
                -p=all                  表示进行全端口扫描：0-65535
                -p=(指定)               表示进行指定端口扫扫描，如：-p=80

            -d                          指定目录扫描
                -d=list.tamper          输出tamper文件夹下目录列表
                -d=list.cms             输出cms文件夹下目录列表
                -d=list.leaks           输出leaks文件夹下目录列表
                -d=(指定)               指定脚本目录扫描，如：-d=jsp
                -d=cms                  进行开源cms目录扫描(功能暂未实现)
                -d=leaks                进行开源漏洞扫描(功能暂未实现)
                -d=admin                进行后台目录扫描(功能暂未实现)
                -d=common               进行高频使用目录扫描(功能暂未实现)
                -d=other                自定义字典扫描，如：-d=other D://1.txt(功能暂未实现)

            -t                          t参数可以延时扫描，不带该参数扫描速度较快(仅扫描目录可用)

            使用示例：

            -u=www.baidu.com -p=all         进行全HTTP端口扫描

            -us=all -p=all                  批量url扫描HTTP存活端口

            -u=www.baidu.com -p=80 -d=jsp   指定扫描jsp目录

            -u=www.baidu.com -p=all -d=jsp  先扫描全HTTP端口,再自动扫描目录

    *********************************************************************************
    '''.decode("utf-8").encode("gbk")
    print(helps)
    help()


