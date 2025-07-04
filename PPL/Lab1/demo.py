import sys

def func_A(args):
    print('Hello ' + args[0] + ' and ' + args[1])
    
def func_B(args):
    print('Result of a^b: ' + str(int(args[0])**int(args[1])))
def main(args):
    print("Arguments passed to the script:", args)
    if(args[0].isdigit()):
        func_B(args)
    else:
        func_A(args)

if __name__ == "__main__":    
    main(sys.argv[1:])
