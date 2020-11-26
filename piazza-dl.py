# Created December 26th 2019

from argparse import ArgumentParser
from piazza_api import Piazza
from typing import TextIO
import json, sys, time

def to_txt(post):
    pass

def main(argv):
    piazza_code: str = ""
    verbose: bool = False

    # Create argument parser
    parser = ArgumentParser(description="Extract all Piazza visable posts from a class forum into individual .txt files in the current directory. One file per post.")

    # Define mandatory arguments
    parser.add_argument("piazza_code",
                        help="The string of random characters at the end of the URL of your class's Piazza forum. The X's represent what is needed: https://piazza.com/class/XXXXXXXXXXXX?cid=123",
                        nargs=1,
                        metavar="PIAZZACODE")
    parser.add_argument("email",
                        help="The email you use to log into Piazza.",
                        nargs=1,
                        metavar="EMAIL")
    parser.add_argument("password",
                        help="The password you use to log into Piazza.",
                        nargs=1,
                        metavar="PASSWORD")

    # Define optional arguments
    parser.add_argument("-v", "--verbose",
                        help="Toggles verbose mode to recieve more information about what's happening.",
                        action="store_true",
                        dest="verbose")

    # Parse the arguments provided
    args = parser.parse_args()

    # Set verbose flag
    if args.verbose:
        verbose = True
        print("Verbose mode ON")

    # Set piazza code
    piazza_code = args.piazza_code[0]
    if verbose:
        print("Piazza Code recieved: " + piazza_code)

    # Login
    p = Piazza()
    if verbose:
        print("Attempting to login")
    p.user_login(args.email[0], args.password[0])

    # Connect to course
    if verbose:
        print("Connecting to course")
    course = p.network(piazza_code)


    # Retrieve feed(posts)
    if verbose:
        print("Retrieving all visable posts")
    posts = course.iter_all_posts()
    
    # Output to files
    if verbose:
        print("Outputting to files")

    for post in posts:
        try:
            f = open("class_"+ piazza_code + "_post_" + str(post["nr"]) + ".json", 'w')
            f.write(json.dumps(post))
            f.close()

            if verbose:
                print("class_" + piazza_code + "_post_" + str(post["nr"]) + ".json done")

            time.sleep(1)   # after some experimentation it seems piazza servers tolerate 1 request per second
        except OSError as e:
            print(e.strerror, file=sys.stderr)

if __name__ == "__main__":
    main(sys.argv)
