# Title: Bracket Matcher
#
# Description: Checks if brackets in an input file are nested correctly, that is, each opening bracket 
# is followed by its corresponding close bracket.
#
# Author: Harry Baines

import glob

# Directory of input files
input_files_dir = './inputFiles/*.txt'

# List of supported open and close brackets
char_dict = {'[':']', '(':')', '{':'}'}

def get_char_list(filename):
    """ Opens a file, removes newlines, whitespace and letters, and returns a list of characters read. """
    return [ch for ch in open(filename).read() if ch != '\n' if ch != ' ' if not(ch.isalpha())]

def brackets_match(ch_list, filename):
    """ Function that takes a list of bracket characters and returns true if every opening bracket 
          has a corresponding close bracket, and false otherwise.  """
    stack = []
    for ch in char_list:
        if ch in char_dict:
            stack.append(ch)
        else:
            try:
                top = stack.pop()
            except IndexError:
                return "{}: '{}' found but nothing to match with".format(filename, ch)
            if not(ch == char_dict[top]):
                return "{}: Not equal - '{}' doesn't match with '{}' ".format(filename, top, ch)
    
    if len(stack) > 0:
        return "{}: '{}' found, expected '{}'".format(filename, stack[-1], char_dict[ch])
    else:
        return "{}: All brackets match!".format(filename)

# Main - read list of files from directory
if __name__ == "__main__":
    input_files = glob.glob(input_files_dir)
    for filepath in input_files:
        char_list = get_char_list(filepath)
        msg = brackets_match(char_list, filepath.split('/')[-1])
        print(msg)
