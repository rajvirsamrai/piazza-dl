# piazza-dl

piazza-dl is a python3 script that extracts all posts from a course's piazza forum and outputs them to formatted individual .txt files.

A verbose mode exists if you want to see the scripts progress.

## Dependencies
[piazza-api](https://github.com/hfaran/piazza-api)

## Usage
```bash session
python3 piazza-dl.py PIAZZACOURSECODE
```
The piazza course code can be found in the url when visiting your class's forum. It would be where the X's are in this example; https[]()://piazza.com/class/XXXXXXXXXXXXXXXX?cid=123

## Missing functionality
Currently this script doesn't download anything other than text. I might add image/media support in the future or you can submit a pull request.
