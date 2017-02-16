# coding=utf-8
#主流程函数，调度其他函数
import NewOP.backup_folder,backup_mysql,backup_mongo,backup_redis,bakup_gitlab,del_op,log,mkdir,report,scp,timer
def backup():
    print '-'*100
