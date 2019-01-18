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


def hash_string(string):
    return hashlib.sha1(string.encode()).hexdigest()


# 分析如何通过docker命令，解析出命令行flag参数，以及docker命令中的请求参数；
# 分析如何处理具体的flag参数信息，并收集Docker Client所需的配置信息；

# docker run commands:
# Usage: $ docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
# e.g., sudo docker run -i -t --name bridge2 --network abc  ubuntu:16.10 /bin/bash

# 以上Docker请求中的参数分为两类：第一类为命令行参数，即docker程序运行时所需提供的参数，
# 如: -D、--daemon=true、--daemon=false等；第二类为docker发送给Docker Server的实际请求参
# 数，如：ps、pull NAME等。

# 其中选项有两种类型：短选项和长选项，前者以 '-' 作为前导符，后接一个字符；后者以 '--' 作为前导符，后接一个字符串。

# Usage: $ docker exec [OPTIONS] CONTAINER [COMMAND] [ARG...]


def getConfiguration(string):
        parser = argparse.ArgumentParser(description='parse user input')
        parser.add_argument('-i', action="store_true")
        parser.add_argument('-t', action="store_true")
        parser.add_argument('--name', action="store", dest="name")
        parser.add_argument('--network', action="store", dest="network")
        parser.add_argument("IMAGE", type=str, help="the image")
        parser.add_argument("COMMAND", type=str, help="the command")

        args = parser.parse_args(string.split())
#        print args
        return args


def main():
        initdb()

        while (1):
                # docker run commands:
                # Usage: $ docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
                # e.g., sudo docker run -it --name bridge2  ubuntu:16.10 /bin/bash
            cmd = raw_input()

#            cmd = "sudo docker run -i -t --name con1 --network abc  ubuntu:16.10 /bin/bash"
            print cmd
            string = cmd.lstrip('sudo docker run')
            args = getConfiguration(string)

            key = ""

            if args.i:
                key = key + "true" + " "
            else:
                key = key + "false" + " "

            if args.t:
                key = key + "true" + " "
            else:
                key = key + "false" + " "

            key = key + args.network + " " + args.IMAGE

            print key

            # hit or miss
            # value == 0 : no such containers
            # value == 1 : container is running other apps and not available
            # value == 2 : container is available
            value = db.get(key)

            # if the hot container exists
            if value:
                print "hit"
                print("%s %s" % ("value is ", value))
                # if the container is running? 
                # container status: 
                # One of created, restarting, running, removing, paused, exited, or dead

                #if not
                        # use this container to run the #COMMAND
                        # after execution, clean the container
                        # how to clean?

                        # Clean up any threads
                        # Reset static data to type default
                        # Close file descriptors

                        # 可以用container volume来读写

            # if not, run a new container and add meta data to kv store                
            else:
                print "miss"

                # run the container 
                value = hash_string(key)
                db.set(key, value)
                print("%s\n%s : %s" % ("add new key:value", key, value))



if __name__ == "__main__":
    main()

