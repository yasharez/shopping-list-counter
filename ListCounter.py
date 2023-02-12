# Yashar Zafari
# CS 361 - Software Engineering I
# 02/11/2023
# List counter program microservice

# Import libraries
import json

class ListCounter:
  """Class implementation for shopping list counter microservice"""

  def __init__(self, json_str):
    """
    Initialize object with both string and json variables
    of json formatted input string
    """

    self._json_str = json_str
    self._json_obj = json.loads(json_str)

  def get_json_str(self):
    """Get method for json string"""
    return self._json_str

  def get_json_obj(self):
    """Get method for json object"""
    return self._json_obj

  def count_lists(self):
    """
    Counts the number of items in each list type and returns a json
    object containing the count for each list type
    """

    counts = {}

    # Iterate through each sublist and count up the items
    for sublist in self._json_obj['shopping lists']:
      if sublist['items'] is not None:
        counts[sublist['name']] = len(sublist['items']) - 1
      else:
        counts[sublist['name']] = 0
    
    return counts

