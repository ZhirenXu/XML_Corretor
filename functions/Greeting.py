import sys

## print program info
def showInfo():
    print("******************************")
    print("*    XML Correcter v1.0      *")
    print("*     Author: Zhiren Xu      *")
    print("*  published data: 4/23/20   *")
    print("******************************")

## print exit message
# @param    fileOut
#           name of output file
def sysExit():
    print("The program is finished. The output file is located in the same folder with your main.py program. Press enter to exit.")
    key = input()
    sys.exit()
