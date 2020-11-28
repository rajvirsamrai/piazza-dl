# piazza-dl

piazza-dl is a Python3 script that downloads all visable Piazza forum posts for a course into individual JSON files in the current directory. One file per post.

## Dependencies
[piazza-api](https://github.com/hfaran/piazza-api)

## Usage
```bash session
python3 piazza-dl.py [-h] [-v] PIAZZACODE EMAIL [PASSWORD]
```
The piazza course code can be found in the url when visiting your class's forum. It would be where the X's are in this example; https[]()://piazza.com/class/XXXXXXXXXXXXXXXX?cid=123

## Missing functionality
Currently this script doesn't download anything other than JSON. I would like to add image/media support in the future or you can submit a pull request.
