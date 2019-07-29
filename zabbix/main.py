# -*- coding: utf-8 -*-


from zabbix.zabbix_install import zabbix
from zabbix.zabbix_work2 import zabbix_work2
from zabbix.timetodo import collete

if __name__ == "__main__":
    zabb = zabbix()
    zabb.Delete_zabbix()
    zabb.Downdload1()
    zabb.modify_conf()
    zabb.start()

    #work2：设置监听的key-value（监听个别端口）
    bn = zabbix_work2()
    bn.key_value()

    #work1：定时任务，监听自己想要监听的列表（监听自己的列表）
    collete()