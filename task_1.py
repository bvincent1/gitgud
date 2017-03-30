#!/usr/bin/env python3

from sh import git
from random import random

def main():
    git.checkout("task_1")

    f = open("file1.txt", "w")
    f.write("here is a file")
    f.close()

    git.add("file1.txt")
    git.commit('-m "commited new text file1"')
    git.push()

    git.checkout("-")


if __name__ == '__main__':
    main()
