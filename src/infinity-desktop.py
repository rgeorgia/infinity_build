"""
infinity-desktop.py

"""
from subprocess import Popen, PIPE
from .config import SysCmdResult, PkginOpt, PKGIN


def copy_to_rcd():
    pass


def install_packages(packages: list) -> SysCmdResult:
    pkgs = ' '.join(packages)
    p = Popen([PKGIN, PkginOpt.INSTALL.value, pkgs], stderr=PIPE, stdout=PIPE)
    stdout, stderr = p.communicate()

    return SysCmdResult(has_error=bool(stderr), stdout=stdout, stderr=stderr)


def setup_home():
    pass


def slim_theme():
    pass


def update_login_conf():
    pass


def update_rc_conf():
    pass


def update_sudo():
    pass


def update_sysctl_conf():
    pass


def main():
    pass


if __name__ == "__main__":
    main()
