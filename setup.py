"""GitCU Data Mining Project Spring 2016
   Created by: Taylor Andrews
   Modified: 2016/03/31

   Setup directories for the project.
"""
import os

def main():
    required_directories = ['./data/classes', './data/repos', './data/commits']

    for d in required_directories:
        if not os.path.exists(d):
            os.makedirs(d)

if __name__ == '__main__':
    main()
