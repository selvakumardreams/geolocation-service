import sys

def trace(msg):
    """
    Trace log
    """
    console('TRACE', msg)

def debug(msg):
    """
    Debug log
    """
    console('DEBUG', msg)

def info(msg):
    """
    Info log
    """
    console('INFO', msg)

def warn(msg):
    """
    Warn log
    """
    console('WARN', msg)

def error(msg):
    """
    Error log
    """
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


    