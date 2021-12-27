#import pandas as pd
#import numpy as np
import re
#import dateparser
from collections import Counter
import sys

def read_file(file):
    '''Reads Whatsapp text file into a list of strings'''

    x = open(file, 'r', encoding='utf-8')
    # Opens the text file into variable x but the variable cannot be explored yet
    y = x.read()
    # By now it becomes a huge chunk of string that we need to separate line by line
    content = y.splitlines()
    # The splitline method converts the chunk of string into a list of strings
    return content


def clean_file(unclean_chat):
    ''' Cleans new lines, status messages, etc'''
    join = [new_line for new_line in unclean_chat if "joined using this" in new_line]

    # Remove new lines
    new_chat = [new_line.strip() for new_line in unclean_chat]
    print("length of chat is:")
    print(len(chat))

    # Clean out the join notification lines
    new_chat = [new_line for new_line in new_chat if not "joined using this" in new_line]

    # Further cleaning
    # Remove empty lines
    new_chat = [new_line for new_line in new_chat if len(new_line) > 1]
    print("length of clean_chat is:")
    print(len(new_chat))

    # Clean out the left notification lines
    new_chat = [new_line for new_line in new_chat if not new_line.endswith("left")]
    print("length after removing 'lefts' is:")
    print(len(clean_chat))

    return new_chat


if __name__ == '__main__':
    filename = sys.argv[-1]
    chat = read_file(filename)
    len(chat)

    clean_chat = clean_file(chat)
    # Merge messages that belong together
    msgs = []  # message container
    pos = 0  # counter for position of msgs in the container
    """
    Flow:
    For every line, see if it matches the expression which is starting with the format "number(s)+slash" eg "12/"
    If it does, it is a new line of conversion as they begin with dates, add it to msgs container
    Else, it is a continuation of the previous line, add it to the previous line and append to msgs, then pop previous line.
    """

    for line in clean_chat:
        print(line)
        if re.findall("\d+[-]", line):
            msgs.append(line)
            pos += 1
        else:
            print("Somethings wrong with the regex")
            take = msgs[pos - 1] + ". " + line
            msgs.append(take)
            msgs.pop(pos - 1)
    len(msgs)
