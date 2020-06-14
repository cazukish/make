import os
import sys

os.environ['str'] =  "Hello Github Test"

def hello(s):
    return s

text = os.getenv('str')
e = hello(text)

for i in range(1,6):
    print(f"{i}th: {e}")

#branch push and merge

class AnotherHello():
    def __init__(self, greeting="hello another branch"):
        self.hello = greeting

    def say(self):
        return self.hello

cl = AnotherHello("Branch X")

print(cl.say())