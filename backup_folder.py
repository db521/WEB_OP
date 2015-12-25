#!/usr/bin/python
# Filename: Auto Backup tomcat
import os, errno
import datetime, time


def backup():
    print '-------------------------------------------------'
    print "The Scripts Backup Starting,Please waiting ......"
    print
    SOURCE = ['/usr/local/tomcat7/']
    print '%s   : source is %s ' % (datetime.datetime.now(), SOURCE)
    TARGET_DIR = '/data/backup/'
    print '%s   : target_dir is %s ' % (datetime.datetime.now(), TARGET_DIR)
    NAME_FILE = 'tomcat7' + time.strftime('_%H%M%S')
    print '%s   : NAME_FILE is %s ' % (datetime.datetime.now(), NAME_FILE)
    today = TARGET_DIR + time.strftime('%Y%m%d')
    print '%s   : today is %s ' % (datetime.datetime.now(), today)
    TARGET = TARGET_DIR + time.strftime('%Y%m%d') + "/" + NAME_FILE + '.tar'
    print '%s   : TARGET is %s ' % (datetime.datetime.now(), TARGET)
    #zip_command = "zip -qr '%s' %s " % (TARGET, ' '.join(SOURCE))
    tar_command = 'tar -cvzf %s %s ' % (TARGET, ' '.join(SOURCE))
    print '%s   : tar_command is %s ' % (datetime.datetime.now(), tar_command)
    #Scripts Exec process Start
    print
    #Judge TARGET_DIR
    def mkdir_p(TARGET_DIR):
        try:
            if not os.path.exists(TARGET_DIR):
                os.makedirs(TARGET_DIR)  # == makdir -p /data/backup/
                print '%s   : Successfully created Directory %s' % (datetime.datetime.now(), TARGET_DIR)
        except OSError as exc:  # Python >2.5 (except OSError, exc: for Python <2.5)
            if exc.errno == errno.EEXIST and os.path.isdir(TARGET_DIR):
                pass
            else:
                raise

    mkdir_p(TARGET_DIR)
    #Judge today DIR
    if not os.path.exists(today):
        os.mkdir(today)  # make DIRectory
        print '%s   : Successfully created Directory %s' % (datetime.datetime.now(), today)
    #Exec Zip Command to Dir or file
    if os.system(tar_command) == 0:
        print '%s   : Successful backup to %s' % (datetime.datetime.now(), TARGET)
    else:
        print 'Backup Failed !'
        print '%s   : Backup Failed !' % (datetime.datetime.now())
    os.system('sleep 2')
    print
    print '--------------- The scripts Exec Done ------------------'


backup()
