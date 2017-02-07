#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
{{image_name}} was generated using using...

                    .,
                   ,Wt t
                  i#D. ED.                ..       :
                 f#f   E#K:              ,W,     .Et
               .D#i    E##W;            t##,    ,W#t
              :KW,     E#E##t          L###,   j###t
              t#f      E#ti##f       .E#j##,  G#fE#t
               ;#G     E#t ;##D.    ;WW; ##,:K#i E#t
                :KE.   E#ELLE##K:  j#E.  ##f#W,  E#t
                 .DW:  E#L;;;;;;,.D#L    ###K:   E#t
                   L#, E#t      :K#t     ##D.    E#t
                    jt E#t      ...      #G      ..
                                         j

    Container Package Manager - Simple container distribution abstraction.

                    https://github.com/monokal/cpm

"""

import requests

__version__ = "{{image_version}}"
__maintainer__ = "{{image_maintainer_name}}"
__email__ = "{{image_maintainer_email}}"


class Package(object):
    def __init__(self):
        """

        """

        pass

    def __call__(self):
        pass

    def docker_module_installed(self):
        """

        :return:
        """

        url = "https://github.com/docker/docker-py/archive/master.zip"

        response = requests.get(url)

        return False

    def docker_executable_installed(self):
        """

        :return:
        """

        return False

    def docker_run(self):
        """

        :return:
        """

        return False


def main():
    """

    :return:
    """

    package = Package()
    return package()


if __name__ == "__main__":
    main()
