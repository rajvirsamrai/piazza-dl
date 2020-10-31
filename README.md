# piazza-dl

piazza-dl is a python3 script that extracts all posts from a course's piazza forum and outputs them, in their raw format (JSON), to individual files.

A verbose mode exists if you want to see the scripts progress.

## Dependencies
[piazza-api](https://github.com/hfaran/piazza-api)

## Usage
```bash session
python3 piazza-dl.py PIAZZACOURSECODE
```
The piazza course code can be found in the url when visiting your class's forum. It would be where the X's are in this example; https[]()://piazza.com/class/XXXXXXXXXXXXXXXX?cid=123
