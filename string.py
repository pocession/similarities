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

    list1 = [line.strip() for line in file1]
    print("In file1, strings are:", end="")
    print(list1)
    print()

    list2 = [line.strip() for line in file2]
    print("In file2, strings are:", end="")
    print(list2)
    print()

    compare_case_sensitive = set(list1) & set(list2)
    print("Same strings (case sensitive) between file1 and file2 are:",end="")
    print(compare_case_sensitive)
    print()

    file1.close()
    file2.close()

    # Do the whole process again, since the seeker in file1&2 already approaches EOF

    file1 = open(sys.argv[1], 'r')
    file2 = open(sys.argv[2], 'r')

    list1x = [line.strip().casefold() for line in file1]
    list2x = [line.strip().casefold() for line in file2]

    compare_case_insensitive = set(list1x) & set(list2x)
    print("Same strings (case insensitive) between file1 and file2 are:",end="")
    print(compare_case_insensitive)
    print()

    file1.close()
    file2.close()

# run the main program
if __name__ == "__main__":
    main()