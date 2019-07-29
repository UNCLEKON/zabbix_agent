# -*- coding:utf-8 -*-

"""
循环任务，每10秒执行一次

"""
from apscheduler.schedulers.blocking import  BlockingScheduler
from zabbix.zabbix_work import zabbix_work

def collete():
    def job():
        work = zabbix_work()
        work.getport()
        #print("获取数据")

    scheduler = BlockingScheduler()
    #scheduler.add_job(job,"cron",hour=17,minute=0)
    scheduler.add_job(job,'interval', seconds=10)
    scheduler.start()





