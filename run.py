# -*- coding: utf-8 -*

# Copyright (c) 2018 Tony Suo.
# This program is free software; you can redistribute it and/or
# modify it under the terms of version 2 of the GNU General Public
# License as published by the Free Software Foundation.

# 01-Jan-2018   Tony Suo        Created this.


# database lib
import pickledb

# hash function lib
import uuid
import hashlib

# parse lib
import argparse


def initdb():
        global db
        db = pickledb.load('hotC.db', False)
        print "run initdb()!"



def main1():
        initdb()
        print "run main()!"

        while (1):
                # docker run commands:
                # Usage: $ docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
                # e.g., sudo docker run -it --name bridge2  ubuntu:16.10 /bin/bash
                key = raw_input()
                value = db.get(key)

                # if the hot container exists
                if (value):
                        print("%s %s" % ("value is ", value))
                # if not, run a new container and add meta data to kv store
                else:
                        value = hash_string(key)
                        db.set(key, value)
                        print("%s %s %s" % ("add new key/value", key, value))



if __name__ == "__main__":
    main()
