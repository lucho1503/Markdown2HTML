#!/usr/bin/python3
"""
convert a markdown to HTML files
"""
import markdown
import sys
import os.path as path

if __name__ == "__main__":
    if len(sys.argv) < 2:
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