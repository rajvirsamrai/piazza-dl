# Created December 26th 2019

from argparse import ArgumentParser
from piazza_api import Piazza
from typing import TextIO
import sys, time

def main(argv):
    piazza_code: str = ""
    output_path: str = ""
    verbose: bool = False

    # Create argument parser
    parser = ArgumentParser(description="Extract all Piazza posts from a class into a group of json files in the current directory. One file per post.")

    # Define mandatory arguments
    parser.add_argument("piazza_code",
                        help="The string of random characters at the end of the URL of your class's Piazza forum. The X's represent what is needed: https://piazza.com/class/XXXXXXXXXXXX?cid=123",
                        nargs=1,
                        metavar="PIAZZACODE")

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
    p.user_login()

    # Connect to course
    if verbose:
        print("Connecting to course")
    course = p.network(piazza_code)


    # Retrieve feed(posts)
    if verbose:
        print("Retrieving feed (posts)")
    feed = course.get_feed(limit=999999, offset=0)
    cids = [post['id'] for post in feed["feed"]]

    # Output to files
    if verbose:
        print("Outputting to files")
    for cid in cids:
        post = course.get_post(cid)
        try:
            f = open("post_"+str(cid)+".json", 'w')
            f.write(str(post))
            f.close()

            if verbose:
                print("post_" + cid + ".json done")

            time.sleep(1)   # after some experimentation it seems piazza servers tolerate 1 request per second
        except OSError as e:
            print(e.strerror, file=sys.stderr)

if __name__ == "__main__":
    main(sys.argv)