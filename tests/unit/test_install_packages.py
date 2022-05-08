"""
test_install_packages
"""
import pytest
from unittest import TestCase
from testfixtures.mock import call
from testfixtures import Replacer, compare
from testfixtures.popen import MockPopen, PopenBehaviour

from src.infinity_desktop import install_packages
from src.config import PKGIN, PkginOpt, SysCmdResult
from tests.data import pkgin_expected, PkginRespType


class TestInstallPackages(TestCase):
    """Class to test install_packages"""

    def setUp(self):
        self.Popen = MockPopen()
        self.r = Replacer()
        self.r.replace("src.infinity_desktop.Popen", self.Popen)
        self.addCleanup(self.r.restore)

    def test_install_package_not_root(self):
        pkg_list = ["dbus", "fake_package"]
        expected = pkgin_expected(PkginRespType.NOT_ROOT.value)
        self.Popen.set_command(
            [PKGIN, PkginOpt.INSTALL.value, ' '.join(pkg_list)],
            stderr=expected.stderr,
            stdout=expected.stdout,
        )
        result = install_packages(pkg_list)
        assert result.has_error

    def test_package_not_in_repo(self):
        pkg_list = ["fake_package"]
        expected = pkgin_expected(PkginRespType.NOT_IN_REPO.value)
        self.Popen.set_command(
            [PKGIN, PkginOpt.INSTALL.value, ' '.join(pkg_list)],
            stderr=expected.stderr,
            stdout=expected.stdout,
        )
        result = install_packages(pkg_list)
        assert result.has_error

    def test_package_error_installing(self):
        pkg_list = ["fake_package"]
        expected = pkgin_expected(PkginRespType.INSTALL_ERROR.value)
        self.Popen.set_command(
            [PKGIN, PkginOpt.INSTALL.value, ' '.join(pkg_list)],
            stderr=expected.stderr,
            stdout=expected.stdout,
        )
        result = install_packages(pkg_list)
        assert result.has_error
        assert 'errors: 1' in result.stdout.decode()

    def test_package_no_errors(self):
        pkg_list = ["fake_package"]
        expected = pkgin_expected(PkginRespType.NO_ERRORS.value)
        self.Popen.set_command(
            [PKGIN, PkginOpt.INSTALL.value, ' '.join(pkg_list)],
            stderr=expected.stderr,
            stdout=expected.stdout,
        )
        result = install_packages(pkg_list)
        assert not result.has_error
        assert 'warnings: 0, errors: 0' in result.stdout.decode()






