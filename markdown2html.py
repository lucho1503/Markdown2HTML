#!/usr/bin/python3

""" 
convert a markdown to HTML files 
"""
import markdown
import sys
import os.path as path

if __name__ == "__main__":
    st = ""
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        exit(1)
    elif not path.exists(sys.argv[1]):
        sys.stderr.write('Missing ' + sys.argv[1] + '\n')
        exit(1)
    else:
        markdown.markdownFromFile(
            input=sys.argv[1],
            output=sys.argv[2],
            encoding='utf-8',
        )
        exit(0)
        #pass

    #with open(sys.argv[1], 'r') as r:
    #    for line in r.readlines():
    #        st += str(parse(line) + '\n')

    #with open(sys.argv[2], 'w') as w:
    #    for line in st:
    #        writer.write(line)