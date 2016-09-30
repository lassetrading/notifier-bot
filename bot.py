#!/usr/bin/env python3

import pprint
import sys
import time

from tools.stock_checker import StockChecker
from tools import utility


SLEEP_TIME = 5
ITEMS_JSON_FILE = "items.json"


def main():
  utility.log("NotifierBot v1.0\n")

  while True:
    items = utility.read_json(ITEMS_JSON_FILE)
    stock_checker = StockChecker(items)
    report = stock_checker.check()

    pprint.pprint(report)
    #for issue in report:
      #pprint.pprint(items[issue["id"]])

    # check the internet connection
    # send the report through something

    # overwrite item.json current state
    for issue in report:
      item_id = issue["id"]
      items[item_id]["current_existance"] = issue["new_existance"]
      items[item_id]["current_price"] = issue["new_price"]
      items[item_id]["current_stock"] = issue["new_stock"]

    utility.write_json(ITEMS_JSON_FILE, items)
    #pprint.pprint(items)

    time.sleep(SLEEP_TIME)



if '__main__' == __name__:
  try:
    main()
  except KeyboardInterrupt:
    sys.exit(0)
