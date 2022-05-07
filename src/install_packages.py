"""
install_packages.py
"""
from subprocess import Popen, PIPE

PKGIN = "/usr/pkg/bin/pkgin"


def packages_to_install(packages: str) -> tuple:
    """
    install packages
    :param packages:
    :return:
    """
    p = Popen(["pkgin", "in", packages], stderr=PIPE, stdin=PIPE, stdout=PIPE)
    stdout, stderr = p.communicate()
    return stdout, stderr
