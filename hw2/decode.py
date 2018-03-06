import base64
import codecs
with codecs.open('memorandum.txt.swp', 'r', 'utf-8') as f:
    t = f.read().strip()
    data = base64.b64decode(t)
    print data
