"""Utility module."""

import json
import sys

from json import JSONDecoder


def log(str):
  sys.stdout.write(str)

def json_validity_check(seq):
  dct = {}
  for key, value in seq:
    if key in dct:
      raise ValueError("Duplicate key %r in json document" % key)
    else:
      dct[key] = value
  return dct

def read_json(file_name):
  with open(file_name) as data_file:
    data = json.load(data_file, object_pairs_hook=json_validity_check)
  return data

def write_json(file_name, json_data):
  with open(file_name, 'w') as outfile:
    json.dump(json_data, outfile,
              sort_keys=True, indent=4, separators=(',', ': '))
