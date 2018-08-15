#!/usr/bin/env python3
"""Find anagrams of words."""

import json
import sys
from itertools import permutations
from english_words import english_words_lower_alpha_set

def find_anagrams(word: str):
    """Find all one-word anagrams of a word.

    Arg:
        word: a string containing a word to find anagrams of.
    Returns:
        A set containing all anagrams of the word, in lowercase. This is
        guaranteed to at least contain the word itself, provided the
        word passed in is an English word.

    """
    # Find all permutations of the word
    perms = {''.join(p) for p in permutations(word.lower())}

    # Filter out all non-English permutations
    anagrams = {word for word in perms
                if word in english_words_lower_alpha_set}

    # Return the results
    return anagrams

if __name__ == '__main__':
    # Get the arguments as a raw JSON string
    raw_args = sys.argv[1]

    # Parse the raw JSON and return a dictionary of the parsed
    # arguments
    args = json.loads(raw_args)

    # Find anagrams
    results = find_anagrams(args['word'])
