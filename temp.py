import sys
import argparse

def main():
    parser=argparse.ArgumentParser(description='Command line interface for core DS implementation in python')
    parser.add_argument('--sort',action='store',dest='sort_type',
                        help='Choose which sort algorithm to use, available options (quick_sort)')
    args=parser.parse_args()
    if args.sort_type=='quick_sort':
        print("chosen quick_sort as argument")
    else:
        pass

if __name__=="__main__":
    main()