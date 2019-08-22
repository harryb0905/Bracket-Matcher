# Bracket-Matcher
This repository contains the Python code for a simple 'Bracket Matcher' algorithm, originally written in C as part of my Software Development coursework at University.

## Psuedocode

- Read input file into Python (store as consecutive character list, remove unwanted characters)
- Process character list by repeating:
  - If current char is an open bracket, push to stack
  - If current char is a close bracket:
    - Pop most recent char from stack
    - If stack is empty, report error (found close, expected open to match with)
    - Check if current char and popped char match
      - If so, proceed
      - If not, report no match
- If stack isn't empty, report error (found open, expected close to match with)

