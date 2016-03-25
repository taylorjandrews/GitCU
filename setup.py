# GitCU Data Mining Project Spring 2016
# Created by: Taylor Andrews
# Modified: 2016/02/11 
#
# Setup directories for the project.

import os

def main():
    required_directories = ['./data/classes', './data/repos']

    for d in required_directories:
        if not os.path.exists(d):
            os.makedirs(d)

if __name__ == '__main__':
    main()
