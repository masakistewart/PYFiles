import os
import sys
from nested.py import write_to_file

html_boilerplate = """
<!DOCTYPE html>
<html>
    <head>
        <title></title>
    </head>
    <body>
    </body>
</html>
"""
server_boilerplate = """
var express = require('express');
var app     = express()

app.use(express.static('/public'))
"""


# get current working directory
cwd = os.getcwd()


def usage():
    print("PYFI")
    print("")
    print("A Simple File System Creator")
    print("")
    print("Usage: python pyfi.py files/like/this/and/this")
    print("")
    print("Make sure that this is the current working")
    print("working directory that you want the files")
    print("out put!")


# sample command /project/public/js+css+img+views

# os.path.exists
# then
# os.makedir

# get current directory
# cwd = os.getcwd()

def create_file(file_name, path):
    file = open(path +file_name, 'w')
    file.close()


# takes a string that looks like: python+me.py
def file_check(string):
    if "." in string:
        return True
    else:
        return False


def logic_section(args):
    for path in args:
        cwd = os.getcwd()
        print(cwd, 'here')
        files = path.split('/')
        for file in files:
            if "+" in file:
                siblings = file.split("+")
                print(cwd, siblings)
                for sibling in siblings:
                    if file_check(sibling):
                        create_file(sibling, cwd + '/')
                    else:
                        os.mkdir(cwd + "/" + sibling)
            else:
                if file_check(file):
                    create_file(file, cwd + '/')
                    if file == "server.js":
                        write_to_file(cwd+'/', server_boilerplate)
                    elif file == 'index.html':
                        write_to_file(cwd+'/', html_boilerplate)
                elif not os.path.exists(cwd + '/' + file):
                    print(cwd, 'otherHere')
                    os.mkdir(cwd + "/" + file)
                cwd += "/" + file


def main():
    if not len(sys.argv[1:]):
        usage()
        sys.exit(0)

    args = sys.argv[1:]

    if args[0] == '-a':
        path = ['app/public/css+model+fonts+img+js+views', 'app/model+server.js', 'app/public/js/controllers+directives+app.js','app/public/views/templates+index.html' ]
        logic_section(path)
    else:
        logic_section(args)


main()
