#!/usr/bin/env python3
"""Find anagrams of words."""

from itertools import permutations
import json
import logging
import os
import sys
from typing import Set
from english_words import english_words_lower_alpha_set

RESULTS_DIR = '/results/'
LOGS_DIR = '/logs/'


def find_anagrams(word: str) -> Set[str]:
    """Find all one-word anagrams of a word.

    Arg:
        word: a string containing a word to find anagrams of.
    Returns:
        A set containing all anagrams of the word, in lowercase. This is
        guaranteed to at least contain the word itself, provided the
        word passed in is an English word.

    """
    # Find all permutations of the word
    logging.debug("Obtaining all permutations for \"%s\"", word)
    perms = {''.join(p) for p in permutations(word.lower())}

    # Filter out all non-English permutations
    logging.debug("Filtering all permutations for \"%s\"", word)
    anagrams = {word for word in perms
                if word in english_words_lower_alpha_set}

    # Return the results
    return anagrams

if __name__ == '__main__':
    # Set up the logger
    uuid = os.environ['JOB_UUID']
    logs_path = os.path.join(
        LOGS_DIR,
        uuid + '-logs.txt')

    logging.basicConfig(
        filename=logs_path,
        level=logging.DEBUG,
        format='%(levelname)s: %(message)s')

    # Get the arguments as a raw JSON string
    raw_args = sys.argv[1]

    # Parse the raw JSON and return a dictionary of the parsed
    # arguments
    args = json.loads(raw_args)
    word = args['word']

    # Save anagrams
    results_path = os.path.join(
        RESULTS_DIR,
        word + '.txt')

    with open(results_path, 'w') as f:
        for result in find_anagrams(word):
            f.write(result + '\n')
