#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Generated using Container Package Manager (CPM).
# https://github.com/monokal/cpm

import sys
import logging

py_modules = [
    'docker',
]

runtime = "docker"

try:
    logger = logging.getLogger('cpm')
    out = logging.StreamHandler(sys.stdout)
    out.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[cpm] %(message)s")
    out.setFormatter(formatter)
    logger.addHandler(out)
    logging.basicConfig(level=logging.INFO)

except:
    print("Oops! I failed to initialise logging.")
    sys.exit(1)


class Package(object):
    def __init__(self):
        pass

    def __call__(self):
        for module in py_modules:
            if not self.py_module_installed(module):
                self.install_py_module(module)

        if not self.container_runtime_installed(runtime):
            self.install_container_runtime(runtime)

        self.run()

    def py_module_installed(self, module):
        try:
            exec(module + " = __import__(module)")

        except ImportError:
            return False

        except:
            logger.exception("Oops! Something unexpected went wrong.")
            sys.exit(1)

        return True

    def install_py_module(self, module):
        import pip

        logger.info("I'm gonna install the \"%s\" Python module." % module)

        try:
            pip.main(['install', module])

        except:
            logger.exception(
                "Oops! I failed to install the \"%s\" Python module." % module
            )
            sys.exit(1)

    def container_runtime_installed(self, runtime):
        try:
            client = docker.from_env()

        except:
            return False

        return True

    def install_container_runtime(self, runtime):
        return False

    def run(self):
        import docker

        client = docker.from_env()

        response = client.containers.run(
            image="",
            command="",
            detach=False,
            entrypoint="",
            hostname="",
            privileged=False,
            publish_all_ports=False,

        )


package = Package()
package()
