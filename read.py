# Similarities (read two files)
# Usage: python similarities.py file1.txt file2.txt
import sys

def main():
    # Prompt users for correct usages
    argc = len(sys.argv)
    if argc != 3:
        print("Usages: read.py file1.txt file2.txt", end="")
        print()
        exit(1)

    a = open(sys.argv[1], 'r')
    b = open(sys.argv[2], 'r')


    print(a.read())
    print(b.read())
    print()
# run the main program
if __name__ == "__main__":
    main()