import sys
import argparse

def main():
    parser=argparse.ArgumentParser(description='Command line interface for core DS implementation in python')
    parser.add_argument('--sort',action='store',dest='sort_type',
                        help='Choose which sort algorithm to use, available options (quick_sort)')
    parser.add_argument('search',action='store',
                        help='Choose which search algorithm to use, available options (BFS,DFS)')
    parser.add_argument('lists',action='store',
                        help='Choose which search algorithm to use, available options (BFS,DFS)')
    args=parser.parse_args()
    if args.sort_type=='quick_sort':
        print("chosen quick_sort as argument")
    if args.search=='BFS':
        print("chosen BFS as argument")
    if args.lists=='stack':
        print("chosen stack as argument")

if __name__=="__main__":
    main()