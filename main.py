"""Main script"""

import sys
import quick_sort

def main():
    "main function!!"
    try:
        infile = open('input.txt', 'r')
        numbers = infile.readlines()
        infile.close()
    except:
        print('An error occurred while opening/reading file', sys.exc_info()[0])
        sys.exit(1)

    input = []
    for num in numbers:
        num=num.strip()
        if num.isdigit():
            input.append(int(num))
    output=quick_sort.qsort(input,0,len(input)-1)

    try:
        outfile = open('output.txt','w')
        for num in output:
           outfile.write(str(num)+"\n")
    except:
        print('An error occurred while trying to write to file', sys.exc_info()[0])
        sys.exit(1)



if __name__ == "__main__":
    main()