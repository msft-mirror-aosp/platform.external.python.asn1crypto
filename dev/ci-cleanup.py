# coding: utf-8
from __future__ import unicode_literals, division, absolute_import, print_function

import os
import shutil

from . import build_root, other_packages


def run():
    """
    Installs required development dependencies. Uses git to checkout other
    modularcrypto repos for more accurate coverage data.
    """

    print("Removing ci dependencies")
    deps_dir = os.path.join(build_root, 'modularcrypto-deps')
    if os.path.exists(deps_dir):
        shutil.rmtree(deps_dir, ignore_errors=True)

    print("Removing modularcrypto packages")
    for other_package in other_packages:
        pkg_dir = os.path.join(build_root, other_package)
        if os.path.exists(pkg_dir):
            shutil.rmtree(pkg_dir, ignore_errors=True)
    print()

    return True
