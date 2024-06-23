#!/usr/bin/python3
""" distributes an archive to the web servers
"""
from fabric.api import *
import os


host1 = '18.235.248.15'
host2 = '100.25.31.89'
user = 'ubuntu'
env.hosts = [host1, host2]


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
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzvf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception:
        return False
