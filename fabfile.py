from fabric.api import *

def host_type():
    run('uname -s')
    
def apt_update():
    sudo('apt-get update')

def apt_upgrade():
    sudo('apt-get -qy upgrade')

def uptime():
    run('uptime')

def reboot():
    sudo('reboot')
