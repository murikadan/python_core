"""
Main script
"""

import sys
import quick_sort

def main():
    "main function!!"
    try:
        infile = open('input.txt', 'r')
        numbers = infile.readlines()
        infile.close()
    except:
        print('An error occurred while trying to read the file', sys.exc_info()[0])
        sys.exit(1)
    input = []
    for num in numbers:
        input.append(int(num.strip()))
    output=quick_sort.qsort(input)
    try:
        outfile = open('output.txt','w')
        for num in output:
            outfile.write("%s\n" % num)
    except IOError:
        print('An error occurred while trying to write to file')
        sys.exit(1)


if __name__ == "__main__":
    main()