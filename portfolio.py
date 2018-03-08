class Portfolio:

   def __init__(self, name):
      self.name = name
      self.stocks = {}
   
   def add_stock(self, stock_abbr, amount):
      try: 
         self.stocks[stock_abbr] += amount
      except KeyError, e:
         self.stocks[stock_abbr] = amount

   def show_portfolio(self):
      for x in self.stocks:
         print str(self.stocks[x]) + " share(s) of " + x

   def get_stock_amount(self, stock_abbr):
      return self.stocks[stock_abbr]
   def remove_stock(self, stock_abbr, amount):
      try:
         self.stocks[stock_abbr] -= amount
         return 0
      except KeyError, e:
         return -1

