# zabbix客户端自动安装并自动监控端口


Zabbix安装并自动化监控



## v0.1 功能
    功能一：提供监控TCP/UDP端口，在web端直接指定某个端口
    功能二：提供监控的端口写入特定文本中，会在指定时间更新并通过日志形式返回监控的情况，并有触发功能（某个端口掉线了会警告）
    功能三：提供企业微信监控
    

## 开发环境
    centos 7.2(1511)  python 2.7

## 服务端安装
    
    测试建议 2核CPU，2G内存以上.
    服务器操作系统版本要求 centos7.2 centos7.4
    安装之前请关闭防火墙
```
说明：安装请使用

zabbix_slave/zabbix/main.py > /var/log/zabbix_agent_person/person_zabbix.log
```


step1: 修改文件zabbix_work.py下的path2指定端口文件:
```
zabbix_work的path2是功能二，指定我们想要监控的端口写入

path2根据个人情况去更改
本例子和项目中path2=/root/listen_port.txt

vim /root/listen_port.txt

示例格式如下：
80
22
8080
.....

```

step2: 拷修改timetodo.py里面的循环执行时间:
```
示例中为10s

根据个人情况和服务器情况更改
```


