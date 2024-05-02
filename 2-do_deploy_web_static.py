#!/usr/bin/python3
from fabric.api import *
from os import path


env.hosts = ["54.164.5.211", "100.26.122.39"]
env.user = "ubuntu"
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """ a Fabric script that distributes an archive to your web servers"""

    if not path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")

        timestamp = archive_path[-18:-4]
        run(f"sudo mkdir -p /data/web_static/releases/web_static_{timestamp}")
        run(f"sudo tar -xzf /tmp/web_static_{timestamp}.tgz -C \
/data/web_static/releases/web_static_{timestamp}/")
        run(f"sudo rm /tmp/web_static_{timestamp}.tgz")

        # move contents into host web_static
        run(f"sudo mv /data/web_static/releases/web_static_{timestamp}/web_static/* \
/data/web_static/releases/web_static_{timestamp}/")
        # remove extraneous web_static dir
        run(f"sudo rm -rf /data/web_static/releases/\
web_static_{timestamp}/web_static")
        run(f"sudo rm -fr /data/web_static/current")
        run(f"sudo ln -s /data/web_static/releases/web_static_{timestamp}/ \
/data/web_static/current")
    except Exception:
        return False

    return True
