#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Package(object):
    def __init__(self):
        pass

    def __call__(self):
        if not self.container_runtime_installed():
            self.install_container_runtime()

        if not self.python_module_installed():
            self.install_python_module()

        self.docker_run()

    def python_module_installed(self):
        try:
            pass

        except:
            print("Oops.")

    def container_runtime_installed(self):
        return False

    def docker_run(self):
        return False

    def install_python_module(self):
        return False

    def install_container_runtime(self):
        return False


package = Package()
package()
