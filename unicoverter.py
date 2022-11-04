#!/usr/bin/python3

import re, argparse
from bs4 import BeautifulSoup

# Get arguments
parser = argparse.ArgumentParser(description='UniConverter takes as input an html file and converts some of the characters to a similar one in order to avoid detection.')

parser.add_argument("-i", "--input",help="input html file", metavar="", required=True)
parser.add_argument("-o", "--output",help="save output in a html file", metavar="")

args = parser.parse_args()

# Read input
original_html = open(args.input,'r').read()
new_html = BeautifulSoup(original_html, "html.parser")

# Replace chars
target = new_html.find_all(text=re.compile(r'o'))
for o in target:
    o.replace_with(o.replace('o','&#x3BF;'))
target = new_html.find_all(text=re.compile(r'l'))
for l in target:
    l.replace_with(l.replace('l','&#x0399;'))

# Print output
if args.output :
    open(args.output,'w').write(str(new_html))
    print("Saved to file: ",args.output)
else:
    print(new_html)
