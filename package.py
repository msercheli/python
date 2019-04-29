# -*- coding: utf-8 -*-

name = "python"

version = "2.7.5"

authors = ["Guido van Rossum"]

description = \
    """
    The Python programming language.
    """

tools = [
    "2to3",
    "idle",
    "pydoc",
    "python",
    "python2",
    "python2.7",
    "python2.7-config",
    "python2-config",
    "python-config",
    "smtpd.py"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
        env.REZ_BUILD_PROJECT_VERSION = this.version

uuid = "repository.python"
