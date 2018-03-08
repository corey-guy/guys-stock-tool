import utilities.guy_print as guy_print
from menu_actions import *
from portfolio_modules import *

def intro():
    print "Welcome to Guys Stock Tool! A Stock Portfolio maintainence program and information giver...designed by Guy, for Guy!"
  
def show_portfolio(portfolio):
   portfolio.show_portfolio()

intro()
portfolio = load_portfolio.load_portfolio()
while(True):
   action = main_menu.main_menu(portfolio)
   if(action == main_menu_options.ADD_STOCK):
      add_stock.add_stock(portfolio)
   elif(action == main_menu_options.REMOVE_STOCK):
      show_portfolio(portfolio)
      remove_stock.remove_stock(portfolio)
   elif(action == main_menu_options.SHOW_PORTFOLIO):
      show_portfolio(portfolio)
   elif(action == main_menu_options.EXIT):
      exit()
