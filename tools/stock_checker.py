"""Stock checker module."""

import json
import pprint
import sys

from tools import utility


class BaseChecker(object):
  def __init__(self, item):
    self._item = item

  def check(self):
    #utility.log("Checking with: " + self._item["class"] + "\n")
    existance_check_result = self.check_existance()
    price_check_result = self.check_price()
    stock_check_result = self.check_stock()

    # existance: bool
    # stock: int,unknown
    # price: float

    # TODO check the types/values

    result = {
      "existance": existance_check_result,
      "price": price_check_result,
      "stock": stock_check_result,
    }

    return result


# TODO should be in a different file
class MorphsuitsChecker(BaseChecker):
  def check_existance(self):
    return False

  def check_price(self):
    return 0

  def check_stock(self):
    return -1 # unknown


# TODO should be in a different file
class PartyramaChecker(BaseChecker):
  def check_existance(self):
    return False

  def check_price(self):
    return 0

  def check_stock(self):
    return -1 # unknown


class StockChecker(object):
  def __init__(self, items):
    self._items = items

  def checker_initializer(self, item):
    checker_class = getattr(sys.modules[__name__], item["class"])
    return checker_class(item)

  def check(self):
    report = []
    for item_id, item in self._items.items():
      checker = self.checker_initializer(item)
      result = checker.check()

      if self.state_changed(item, result):
        change = {
          "id": item_id,
          "new_existance": result["existance"],
          "new_price": result["price"],
          "new_stock": result["stock"]
        }
        report.append(change)
    return report

  def state_changed(self, item, new_state):
    if item["current_existance"] != new_state["existance"] or \
       item["current_price"] != new_state["price"] or \
       item["current_stock"] != new_state["stock"]:
      return True


