#!/usr/bin/env python3

from sh import git
from random import random

def main():
    git.checkout("-b", "task_1")

    f = open("file1.txt", "w")
    f.write("here is a file")
    f.close()
    git.commit("-am", "commited new text file1")
    git.push("--set-upstream", "origin", "task1")

    git.checkout("-")


if __name__ == '__main__':
    main()
