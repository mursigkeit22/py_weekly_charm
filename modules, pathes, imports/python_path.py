import sys
#As initialized upon program startup, the first item of this list, path[0],
# is the directory containing the script that was used to invoke the Python interpreter.
# If the script directory is not available (e.g. if the interpreter is invoked interactively or
# if the script is read from standard input),  path[0] is the empty string,
# which directs Python to search modules in the current directory first.

# sys.path always includes the path of the script invoked on the command line
# and is agnostic to the working directory on the command line.
for path in sys.path:
    print(path)
