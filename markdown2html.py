#!/usr/bin/python3
import markdown
import sys
import os.path as path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: ./markdown2html.py README.md README.html')
        exit(1)
    if not path.exists(sys.argv[1]):
        print('Missing <filename>')
        exit(1)
    markdown.markdownFromFile(
        input=sys.argv[1],
        output=sys.argv[2],
        encoding='utf-8',
    )
    exit(0)