from urllib import parse
import fileinput
import re
 
# cat e100.md | python link_replace.py | tee ./README.md

bg_pre = 'http://www.biblegateway.com/passage/?'
query_str = {'language':'en'}
versions = ['NIV','MSG']

def bg_link(verse, version='all'):
    verse = verse.group()
    output = '*{}*'.format(verse)

    if version == 'all':
        for ver in versions:
            query_str['search'] = verse
            query_str['version'] = ver
            output += ' [{0}] ({1})'.format(ver,bg_pre + parse.urlencode(query_str))
        return(output)

if __name__ == '__main__':
    for line in fileinput.input():
        line = re.sub(r'(?<=\*\*\s).*$', bg_link, line)
        print(line, end='')
