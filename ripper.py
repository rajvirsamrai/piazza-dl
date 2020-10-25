# Created December 26th 2019
from piazza_api import Piazza
from typing import TextIO
import time

course_code=""
course_piazza_code=""

p = Piazza()
p.user_login()
user_profile = p.get_user_profile()
course = p.network(course_piazza_code)

feed = course.get_feed(limit=999999, offset=0)
cids = [post['id'] for post in feed["feed"]]

for cid in cids:
    post = course.get_post(cid)
    f = open(course_code+"_post_"+str(cid), 'w')
    f.write(str(post))
    f.close()
    print(cid + " done")
    time.sleep(1)   # after some experimentation it seems piazza servers tolerate 1 request per second

