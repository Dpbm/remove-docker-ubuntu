#!/bin/python3

import os
import sys

USER = os.environ.get("SUDO_USER")
HOME = f'/home/{USER}'
RED = "\033[31m"
ZSHRC = f'{HOME}/.zshrc'


def remove_from_apt():
    try:
        os.system('apt-get purge docker-ce docker-ce-cli containerd.io docker-compose-plugin docker docker-engine docker.io containerd runc')
        os.system('apt autoremove')
    except:
        print(f"\n{RED} Failed on remove packages! \n")


def remove_files():
    try:
        os.system('rm -rf /var/lib/docker*')
        os.system('rm -rf /var/lib/containerd*')
        os.system('rm -rf /etc/apt/sources.list.d/docker.list')
        os.system('rm -rf /etc/apt/keyrings/docker.gpg')
        os.system('rm -rf /etc/docker*')
        os.system('rm -rf /var/docker*')
        os.system('rm -rf /var/cache/apt/archives/docker*')
        os.system('rm -rf /run/docker*')
        os.system(
            'rm -rf /usr/lib/python3/dist-packages/sos/report/plugins/__pycache__/docker*')
        os.system(
            'rm -rf /usr/lib/python3/dist-packages/sos/report/plugins/docker*')
        os.system(
            'rm -rf /usr/lib/python3/dist-packages/sos/policies/runtimes/docker*')
        os.system(
            'rm -rf /usr/lib/python3/dist-packages/sos/policies/runtimes/__pycache__/docker*')
        os.system('rm -rf /usr/share/perl5/NeedRestart/CONT/docker*')
    except:
        print(f"\n{RED} Failed on remove files! \n")


def stop_sockets():
    try:
        os.system('systemctl stop docker.socket')
    except:
        print(f"\n{RED} Failed on stop docker.socket! \n")


def delete_groups():
    try:
        os.system('groupdel docker')
    except:
        print(f"\n{RED} Failed on delete docker group! \n")


def upgrade():
    try:
        os.system('apt update')
        os.system('apt upgrade -y')
    except:
        print(f"\n{RED} Failed on upgrade repositories! \n")


def delete_interfaces():
    try:
        interfaces = os.listdir('/sys/class/net')
        for interface in interfaces:

            if('docker' in interface):
                os.system(f'ip link delete {interface}')

    except:
        print(f"\n{RED} Failed on delete interfaces! \n")


def main():
    remove_from_apt()
    remove_files()
    stop_sockets()
    delete_groups()
    upgrade()
    delete_interfaces()


if __name__ == '__main__':
    user_type = os.getuid()

    if(user_type != 0):
        print(f"\n{RED} Please Run as Root! \n")
        sys.exit(1)

    main()
