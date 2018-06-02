"""
Main script
"""

import quick_sort

def main():
    "main function!!"
    infile = open('input.txt', 'r')
    numbers = infile.readlines()
    infile.close()
    input = []
    for num in numbers:
        input.append(int(num.strip()))
    output=quick_sort.qsort(input)
    outfile = open('output.txt','w')
    for num in output:
        outfile.write("%s\n" % num)


if __name__ == "__main__":
    main()