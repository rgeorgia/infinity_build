"""
data.py
Data used as expected for pytest
"""
from dataclasses import dataclass
from enum import Enum
from typing import Type


class PkginRespType(Enum):
    NOT_ROOT = 1
    NOT_IN_REPO = 2
    INSTALL_ERROR = 3
    NO_ERRORS = 4


@dataclass
class Result:
    stdout: bytes
    stderr: bytes


def pkgin_expected(resp_type: int) -> Type[Result]:

    match resp_type:
        case PkginRespType.NOT_ROOT.value:
            Result.stderr = b"pkgin: You don't have enough rights for this operation.\n"
            Result.stdout = b""
            return Result
        case PkginRespType.NOT_IN_REPO.value:
            Result.stderr = b" is not available in the repository"
            Result.stdout = b"calculating dependencies...done.\nnothing to do."
            return Result
        case PkginRespType.INSTALL_ERROR.value:
            Result.stderr = b"not installed"
            Result.stdout = b"pkg_install warnings: 0, errors: 1"
            return Result
        case PkginRespType.NO_ERRORS.value:
            Result.stderr = b""
            Result.stdout = b"pkg_install warnings: 0, errors: 0\reading local summary...\nprocessing local summary...\nmarking PACKAGE as non auto-removable"
            return Result
        case _:
            Result.stderr = b""
            Result.stdout = b""
            return Result


