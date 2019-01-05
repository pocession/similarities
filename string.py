# Similarities (compare string between two files)
# Usage: python string.py file1.txt file2.txt
import sys

def main():
    # Prompt users for correct usages
    argc = len(sys.argv)
    if argc != 3:
        print("Usages: string.py file1.txt file2.txt", end="")
        print()
        exit(1)

    file1 = open(sys.argv[1], 'r')
    file2 = open(sys.argv[2], 'r')



    for line in file1:

    for line in file2:



# run the main program
if __name__ == "__main__":
    main()