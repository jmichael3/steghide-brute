#!/usr/bin/env python

import sys
import subprocess

if __name__ == "__main__":
    # do magic
    if len(sys.argv) != 3:
        print("\n[*]Usage: {} <image_file> <wordlist>\n".format(sys.argv[0]))
        sys.exit()
    else:
        with open(sys.argv[2], "r") as f:
            for _ in f.readlines():
                print("[*]Trying... {}".format(_))
                try:
                    # steghide extract -sf image.jpg -p password123
                    subprocess.check_output(
                        "steghide extract -sf {} -p {}".format(sys.argv[1], _), shell=True)
                    print("[+]Success : {}".format(_))
                    sys.exit()
                except Exception as e:
                    print("[-]Fail!!!")
