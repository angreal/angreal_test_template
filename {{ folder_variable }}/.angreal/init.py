import sys
green = "\33[32m"
red = "\33[31m"
end = "\33[0m"

def init():
    print(green + "=" * 20  + end, file=sys.stderr )
    print(green + "INITIALIZING OUR PROJECT!!" + end, file=sys.stderr)
    print(green + "=" * 20  + end , file=sys.stderr)
