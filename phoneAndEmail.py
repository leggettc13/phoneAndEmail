#! /usr/bin/python3

# phoneAndEmail.py - A program that gets text off of the clipboard, Finds
# all the phone numbers and email addresses in the text, and then pastes
# them onto the clipboard.

import pyperclip, re

# TODO: Create Phone Number regex.

phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?              # area code
        (\s|-|\.)?                      # separator
        (\d{3})                         # first 3 digits
        (\s|-|\.)                       # separator
        (\d{4})                         # last 4 digits
        (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # extension
        )''', re.VERBOSE)

print(phoneRegex.search("(252) 296-6281 ext. 24").group())

# TODO: Create Email regex.

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.
