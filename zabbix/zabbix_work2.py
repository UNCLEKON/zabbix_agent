#coding = utf-8

import os,subprocess
from zabbix.zabbix_install import path1

class zabbix_work2():
    # def check(self,portl):
    #
    #     cmd = "lsof -i:{port} ".format(port=portl)
    #     process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    #     yy = process.stdout.read()
    #     if yy == b'':
    #         tt = 0
    #         print("端口不在监听")
    #
    #     else:
    #         tt = 1
    #         print("端口在监听")


    def key_value(self):
        if os.path.exists('/usr/bin/netstat'):
            pass
        else:
            os.system('yum -y install netstat-tools')

        os.system('touch /tmp/port.sh')
        os.system("echo 'x=`netstat -tunlp|grep :$1|wc -l`;if [ $x -ne 0 ];then echo 1;else echo 0;fi' > /tmp/port.sh")
        key1 = "port.listen[*]"
        value2 = "/bin/bash /tmp/port.sh $1"
        key_value1 = "echo 'UserParameter={keyname},{value}'".format(keyname=key1, value=value2)
        os.system('{action} >> {path}'.format(action=key_value1, path=path1))
        os.system('cat /etc/zabbix/zabbix_agentd.conf|grep "UserParameter="')
        os.system('chmod +s /bin/netstat')
        os.system('systemctl restart zabbix-agent')


