#! /usr/bin/python3

# phoneAndEmail.py - A program that gets text off of the clipboard, Finds
# all the phone numbers and email addresses in the text, and then pastes
# them onto the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?              # area code
        (\s|-|\.)?                      # separator
        (\d{3})                         # first 3 digits
        (\s|-|\.)                       # separator
        (\d{4})                         # last 4 digits
        (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # extension
        )''', re.VERBOSE)

emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+   # username
        @                   # @ symbol
        [a-zA-Z0-9.-]+      # domain name
        (\.[a-zA-Z]{2,4})   # dot-something (.com, .net, etc)
        )''', re.VERBOSE)

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.
