import os
import sys

os.environ['str'] =  "Hello Github Test"

def hello(s):
    return s

text = os.getenv('str')
e = hello(text)

for i in range(1,6):
    print(f"{i}th: {e}")