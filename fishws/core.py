# -*- coding: utf-8 -*-
from . import helpers


def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def command_line_runner():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())
