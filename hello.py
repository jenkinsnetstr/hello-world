#!/usr/bin/env python

def greetings(string):
    if string == "hello":
        print "**Greetings from hello Function**"
        print 
        print "hello :)"
        print "Welcome to world of python"
        print
        print "**End of Greetings from hello Function**"
    else:
        print 
        print "hi, thanks for greetings. Welcome to python."
        print

def status(some_string):
    print some_string
    if some_string == "working":
        return "Still Logged In"
if __name__ == '__main__':
    greetings("hello")
    greetings("working")
