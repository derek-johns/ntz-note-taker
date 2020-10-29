# add your code in this file
import os
import sys


# main function
def cli():
    print(get_args())


def get_args():
    """Get arguments entered by user"""
    if len(sys.argv) <= 1:
        return -1
    return sys.argv


# run the main function
cli()
