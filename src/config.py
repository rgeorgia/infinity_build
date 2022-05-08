"""
config.py

Holds config 'global' data
"""
from dataclasses import dataclass
from enum import Enum


class ErrorCodes(Enum):
    NO_ERROR = 0
    APP_ERROR = 1
    SYS_ERROR = 2
    UNKNOWN = 3


class PkginOpt(Enum):

    INSTALL = 'in'
    LIST = 'ls'
    SEARCH = 'se'
    REMOVE = 'rm'


@dataclass
class SysCmdResult:
    has_error: bool
    stdout: bytes
    stderr: bytes


PKGIN = 'pkgin'


SERVICES_TO_INSTALL = ["dbus", "avahi", "hal", "famd"]
SERVICES_TO_START = [
    "dbus",
    "hal",
    "rpcbind",
    "famd",
    "avahidaemon",
]

DEFAULT_RC_DOT_CONF = {
    "ipv6addrctl": "YES",
    "ipv6addrctl_policy": "ipv4_prefer",
    "sshd": "YES",
    "ntpd": "YES",
    "wscons": "YES",
    "microcode": "YES",
    "zfs": "YES",
    "snort": "NO",
    "dbus": "YES",
    "hal": "YES",
    "rpcbind": "YES",
    "famd": "YES",
    "avahidaemon": "YES",
    "samba": "NO",
    "nmbd": "NO",
    "smbd": "NO",
    "winbindd": "NO",
    "slim": "YES",
    "xdm": "NO",
}

DIR_HOME_LIST = [
         "Documents",
         "Pictures/backgrounds",
         "Downloads",
         "Templates",
         "Desktop",
         "Videos",
         "workspace",
         "bin",
         "nowhere",
     ]

