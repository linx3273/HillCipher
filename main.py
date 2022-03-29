import sys
import src.usage as usage
import src.msgs as msgs
import src.matrixop as matrixop
import src.generateKey as generatekey

def main():
    if len(sys.argv) < 2:
        print(usage.inf())

    elif len(sys.argv) > 4:
        msgs.errmsg("Too many arguments provided. Run 'hillcipher --help'")

    else:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print(usage.inf())
      
        elif sys.argv[1] == "encrypt" or sys.argv[1] == "e":
            if len(sys.argv) == 3 and (sys.argv[2] == "--help" or sys.argv[2] == "-h"):
                print(usage.encInf())

            elif len(sys.argv) == 4:
                matrixop.cryptHandler(sys.argv[3],generatekey.buildKeyMatrix(sys.argv[2]),1)

            else:
                msgs.errmsg("Invalid/Missing Arguments. Run 'hillcipher encrypt --help'")

        elif sys.argv[1] == "decrypt" or sys.argv[1] == "d":
            if len(sys.argv) == 3 and (sys.argv[2] == "--help" or sys.argv[2] == "-h"):
                print(usage.decInf())

            elif len(sys.argv) == 4:
                matrixop.cryptHandler(sys.argv[3],generatekey.buildKeyMatrix(sys.argv[2]),0)

            else:
                msgs.errmsg("Invalid/Missing Arguments. Run 'hillcipher decrypt --help'")

        else:
            msgs.errmsg("Invalid arguments provided. Run 'hillcipher --help'")

if __name__ == "__main__":
    main()