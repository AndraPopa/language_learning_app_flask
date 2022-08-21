"""
Implements the model of our website by simulating a database.

Don't do this in a real world application. Use a database layer!
"""

import json


def load_db():
    with open('flashcards_db.json') as f:
        return json.load(f)


db = load_db()
