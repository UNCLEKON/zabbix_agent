# -*- coding: utf-8 -*-

"""
zabbix_agent自动安装

配置需要做如下修改：
IP
Hostname
UnsafeUserParameters=1 # 默认为0，表示不允许自定义key

"""


import os,sys,json,re
import socket,paramiko
import subprocess,shutil

""""
#ansible，暂时不用

import ansible.playbook
from ansible.inventory.manager import InventoryManager # 用于导入资产文件
from ansible import utils
from ansible.vars.manager import VariableManager  # 用于存储各类变量信息
from ansible.parsing.dataloader import DataLoader # 用于读取YAML和JSON格式的文件
from ansible.inventory.host import Host # 操作单个主机信息
from ansible.inventory.group import Group # 操作单个主机信息
from ansible.playbook.play import Play # 存储执行hosts的角色信息
from ansible.executor.task_queue_manager import TaskQueueManager # ansible底层用到的任务队列
from ansible.executor.task_executor import  TaskExecutor # 核心类执行playbook
"""



"""
不需要用到的模块

#下面是远程连接zabbix server

#新建客户端对象
myclient = paramiko.SSHClient()
#设置成默认自动接受密钥
myclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接远程主机
myclient.connect(hostname,port=22,username="root",password="1")  #密码暴露不安全需要优化
#在远程机执行shell命令
stdin, stdout, stderr = client.exec_command("ls -l")
#读返回结果
print stdout.read()
# 在远程机执行python脚本命令
stdin, stdout, stderr = client.exec_command("python /home/test.py")

"""

#安装zabbix—agent

"""
1.删除zabbix
2.配置镜像源或者直接镜像源安装
3.修改配置（IP）

"""

#变量：
url1 = "https://mirrors.tuna.tsinghua.edu.cn/zabbix/zabbix/3.2/rhel/7/x86_64/zabbix-agent-3.2.11-1.el7.x86_64.rpm"
path1 = "/etc/zabbix/zabbix_agentd.conf"
key = "https://mirrors.tuna.tsinghua.edu.cn/epel/RPM-GPG-KEY-EPEL-7"



    # IP & hostname

hostname = socket.gethostname()
addr = socket.gethostbyname(hostname)
print("【info】服务器IP和主机名如下：")
print(addr, hostname)  # test


class zabbix():

    def Delete_zabbix(self):
        # 卸载原有的，不管有没有
        print("【info】开始zabbix_agent安装进程：\n")
        os.system('systemctl stop zabbix-agent')
        os.system('ps -aux|grep zabbix-agent')
        print("【info】安装包如下：")
        os.system('rpm -qa |grep zabbix')
        if os.path.exists(path1):
            print("【info】执行卸载命令前，zabbix配置存在,一部分配置如下:")
            os.system('cat %s |grep Server' % path1)
            os.system('cat %s |grep Hostname' % path1)
            os.system('cat %s |grep "UnsafeUserParameters="' % path1)

            print("【info】原来配置展示完毕，开始删除")
        else:
            print("【info】执行卸载命令前，zabbix配置不存在")

        print("【info】zabbix 开始被移除")
        print("【info】卸载zabbix各种包")
        os.system('yum -y remove zabbix-*')
        #os.system('rpm -e zabbix*')
        print("【info】zabbix 已经被移除")
        if os.path.exists(path1):
            os.remove(path1)
            print("【info】zabbix配置已删除")
        else:
            print("【info】zabbix配置不存在")
        print("【info】zabbix has been removed")

    def Downdload1(self):
    #依赖安装
        print("【info】zabbix:安装各种依赖中")
        subprocess.call(["yum","-y","install","OpenIPMI-libs","fping","iksemel","unixODBC","net-snmp"])


        os.system('rpm --import %s'%key) #下载时需要的证书
        os.system('rpm -ivh %s'%url1)    #下载zabbix——agent


    def modify_conf(self):
        #修改配置文件中的serverip和hostname
        if  os.path.exists(path1):
            print("【info】配置存在,原配置中IP信息如下：")
            os.system('cat %s |grep Server=' % path1)
            print("【info】配置存在,原配置中Hostname信息如下：")
            os.system('cat %s |grep "Hostname="' % path1)
            print("【info】配置存在,原配置中UnsafeUserParameters信息如下：")
            os.system('cat %s |grep "UnsafeUserParameters="' % path1)

            #更改操作
            os.system("sed -i 's/=127.0.0.1/=10.4.2.16/g' %s" %path1)      #服务端IP地址
            os.system("sed -i 's/=Zabbix server/={host}/g' {p} ".format(host=hostname,p=path1))
            os.system("sed -i 's/UnsafeUserParameters=0/UnsafeUserParameters=1/g' %s"%path1)


            #IP配置
            print("【info】配置存在,更改后配置中IP信息如下：")
            os.system('cat %s |grep "Server="'%path1)


            #hostname配置；
            print("【info】配置存在,更改后配置中hostname信息如下：")
            os.system('cat %s |grep "Hostname="' % path1)

            #设置UnsafeUserParameters=1 # 默认为0，表示不允许自定义key
            print("【info】配置存在,更改后配置中UnsafeUserParameters信息如下")
            os.system('cat %s |grep "UnsafeUserParameters="' % path1)

            return 1
            # with open(path1,'r+',encoding="utf-8") as f1:
            #     for line in f1:
            #         line.write(re.sub("127.0.0.1","192.168.115.138"))
            #         line.write(re.sub("=zabbix server", "=%s"%hostname))




        else:
            print("【info】配置不存在，安装有异常！！")
            return 0


    def start(self):
        #启动程序
        os.system('iptables -F')
        os.system('setenforce 0')
        try:
            os.system('systemctl restart zabbix-agent')
            print("【info】zabbix启动成功")
            print("【info】zabbix进程如下：")
            os.system('ps -aux|grep zabbix')

        except:
            print("【info】zabbix启动失败请检查！")


