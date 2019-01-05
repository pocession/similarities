# Similarities (compare line numbers between two files)
# Usage: python lines.py file1.txt file2.txt
import sys

def main():
    # Prompt users for correct usages
    argc = len(sys.argv)
    if argc != 3:
        print("Usages: lines.py file1.txt file2.txt", end="")
        print()
        exit(1)

    file1 = open(sys.argv[1], 'r')
    file2 = open(sys.argv[2], 'r')

    line_num_1 = 0
    line_num_2 = 0

    for line in file1:
        line_num_1 += 1
    for line in file2:
        line_num_2 += 1
    if line_num_1 == line_num_2:
        print("Both files have {i} lines.".format(i = line_num_1), end="")
        print()
    if line_num_1 != line_num_2:
        print("file1 has {i} lines but file2 has {j} lines.".format(i = line_num_1, j = line_num_2), end="")
        print()

# run the main program
if __name__ == "__main__":
    main()