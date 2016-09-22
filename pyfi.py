import os
import sys

# the problem I am facing is that once the branch splits how can I continue the tree?
# can I also do it using recursion?




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

def create_file(file_name):
    file = open(file_name, 'w')
    file.close()


# takes a string that looks like: python+me.py
def file_check(string):
    if "." in string:
        return True
    else:
        return False


    # currently broken need to fix the passing of cwd from function to function
    # also build another set of functions to handle branching and subfiles
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
                        create_file(sibling)
                    os.mkdir(cwd + "/" + sibling)
            else:
                if file_check(file):
                    create_file(file)
                elif not os.path.exists(cwd + '/' + file) and not "." in file:
                    print(cwd, 'otherHere')
                    os.mkdir(cwd + "/" + file)
                cwd += "/" + file

def main():
    if not len(sys.argv[1:]):
        usage()
        sys.exit(0)

    args = sys.argv[1:]

    if args[0] == '-a':
        path = ['app/public/css+model+fonts+img+js+views', 'app/server.js', 'app/public/views/templates+index.html', 'app/public/js/controllers+directives+app.js' ]
        logic_section(path)
    else:
        logic_section(args)


main()
