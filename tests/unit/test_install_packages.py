"""
test_install_packages
"""
import pytest
from unittest import TestCase
from testfixtures.mock import call
from testfixtures import Replacer, compare
from testfixtures.popen import MockPopen, PopenBehaviour

from src.install_packages import packages_to_install


class TestInstallPackages(TestCase):
    """Class to test install_packages"""
    def setUp(self):
        self.Popen = MockPopen()
        self.r = Replacer()
        self.r.replace("src.install_packages.Popen", self.Popen)
        self.addCleanup(self.r.restore)

    def test_packages_to_install_not_root(self):
        pkg_list = " ".join(['pkg_fake', 'dbus'])
        stderr_expected = b"pkgin: You don't have enough rights for this operation.\n"
        self.Popen.set_command(['pkgin', 'in', pkg_list], stderr=stderr_expected)
        stdout, stderr = packages_to_install(pkg_list)
        assert bool(stderr)
        assert stderr == stderr_expected

    def test_package_not_in_repo(self):
        pkg_list = "fake_package"
        stderr_expected = f"{pkg_list} is not available in the repository".encode()
        stdout_expected = b"calculating dependencies...done.\nnothing to do."
        self.Popen.set_command(['pkgin', 'in', pkg_list], stdout=stdout_expected, stderr=stderr_expected)
        stdout, stderr = packages_to_install(pkg_list)
        assert bool(stderr)
        assert bool(stdout)
        assert stderr == stderr_expected
        assert stdout == stdout_expected
