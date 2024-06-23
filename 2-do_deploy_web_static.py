#!/usr/bin/python3
""" distributes an archive to the web servers
"""
from fabric.api import *
import os


host1 = '18.235.248.15'
host2 = '100.25.31.89'
user = 'ubuntu'
env.hosts = [host1, host2]
env.user = user
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """ Deploys web_static content after uncompressing
    The tar file identified in archive_path.

        Args:
            archive_path(str): The local archrive path
        Returns:
            bool: True if everything was successfully
                executed. Returns False otherwise,
                or when the archive_path does not exist.
    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        name_no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run(f'mkdir -p {path}{name_no_ext}/')
        run(f'tar -xzvf /tmp/{file_name} -C {path}{name_no_ext}/')
        run(f'rm /tmp/{file_name}')
        run(f'mv {path}{name_no_ext}/web_static/* {path}{name_no_ext}/')
        run(f'rm -rf {path}{name_no_ext}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {path}{name_no_ext}/ /data/web_static/current')
        return True
    except Exception:
        return False
