#!/usr/bin/python3
# 7-islower.py
# Ajulor S Moses <mosesajulor@gmail.com>


def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
