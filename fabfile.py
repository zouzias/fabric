from fabric.api import *

env.hosts = ['host1', 'host2']
env.use_ssh_config = True

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
