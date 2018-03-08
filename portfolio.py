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
