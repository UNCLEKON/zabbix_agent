import os,subprocess
from zabbix.zabbix_install import path1

""""
listen_port.txt文件记载了需要监控的端口号

'"""
path2 = "/root/listen_port.txt"


class zabbix_work():
    def getport(self):
        if os.path.exists(path2):
            #print("listen_port.txt文件存在")
            file = open(path2,'r+')
            lines = file.read()
            #print(lines)
            spl = lines.split('\n')[0:-1]
            #print(spl)

            if os.path.exists('/tmp/port.txt'):
                pass
                os.system('echo "" >/tmp/port.txt')
            else:
                os.system('touch /tmp/port.txt')


            for port in spl:
                #print(port)
                #cmd = "netstat -tunlp|grep {port} ".format(port=':'+port+' ')
                cmd = "lsof -i:{port1} ".format(port1=port)
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True)
                #print(process.stdout.read())
                xxx = process.stdout.read()
                ff = open("/tmp/port.txt",'a+')
                if xxx == b'':
                    taget = 0
                    #print("{x}:{y}".format(x=port,y=taget))
                    vv = "{port}:{tag}".format(port=port,tag=taget)
                    ff.write(vv)
                    ff.write("\n")
                    #os.system('echo {thing} >> {path22}'.format(thing=vv,path22=path2))
                    print(ff.read())
                    #print(dirt)

                else:
                    taget = 1
                    vv = "{port}:{tag}".format(port=port, tag=taget)
                    ff.write(vv)
                    ff.write("\n")
                    #os.system('echo {thing} >> {path22}'.format(thing=vv, path22=path2))
                    print(ff.read())
                    #print("{x}:{y}".format(x=port,y=taget))

                print(ff.read())
                ff.close()
            os.system('cat /tmp/port.txt')



        else:
            print("listen_port.txt不存在,或路径不在/root/listen_port.txt")


"""
这部分不需要，因为监听列表部分施舍zabbix日志监控
"""

    # def key_value(self):
    #     key1 = "port.listen[*]"
    #     value2 = "cat /tmp/port.txt|grep $1|cut -d':' -f2"
    #     key_value1 = "echo 'UserParameter={keyname},{value}'".format(keyname=key1,value=value2)
    #     os.system('{action} >> {path}'.format(action=key_value1,path=path1))
    #     os.system('cat /etc/zabbix/zabbix_agentd.conf|grep "UserParameter="')
    #     os.system('systemctl restart zabbix-agent')


