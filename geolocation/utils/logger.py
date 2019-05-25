import sys

def trace(msg):
    console('TRACE', msg)

def debug(msg):
    console('DEBUG', msg)

def info(msg):
    console('INFO', msg)

def warn(msg):
    console('WARN', msg)

def error(msg):
    console('ERROR', msg)

def console(tag, msg, newline=True, stream='stdout'):
    """
    Writes the message to the console.
    """
    msg = tag + ": " + msg
    if newline:
        msg += '\n'
    stream = sys.__stdout__ if stream.lower() != 'stderr' else sys.__stderr__
    stream.write(msg)
    stream.flush


    