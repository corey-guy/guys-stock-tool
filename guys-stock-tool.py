import utilities.guy_print as guy_print
import portfolio as p
import utilities.main_menu_options as main_menu_options

def intro():
    print "Welcome to Guys Stock Tool! A Stock Portfolio maintainence program and information giver...designed by Guy, for Guy!"
  
def load_portfolio():
   option_is_valid = False
   guy_print.print_with_dashes("What do you want to do?\n1.Start a New Portfolio\n2.Load Existing Portfolio")
   while(option_is_valid != True):
      input = raw_input()
      if(input == "1"):
         guy_print.print_with_dashes("Starting a New Portfolio")
         option_is_valid = True
         return p.Portfolio("New Portfolio")
      elif(input == "2"):
         guy_print.print_with_dashes("Please Select a Portfolio")
         option_is_valid = True
      else:
         guy_print.print_retry_message()
   

def main_menu(portfolio):
   option_is_valid = False
   guy_print.print_with_dashes("What do you want to do with " + portfolio.name + "?\n1.Add Stock\n2.Show Portfolio\nOR\n3.Exit Program")
   while(option_is_valid != True):
      input = raw_input()
      if(input == "1"):
         return main_menu_options.ADD_STOCK
      elif(input == "2"):
         return main_menu_options.SHOW_PORTFOLIO
      elif(input == "3"):
         return main_menu_options.EXIT
      else:
         guy_print.print_retry_message()

def add_stock(portfolio):
   guy_print.print_with_dashes("What stock would you like to add? Please use ticker letters. Example: MSFT")
   stock_abbr = raw_input()
   guy_print.print_with_dashes("How much of that stock would you like to add? Numbers only")
   amount  = input()
   #portfolio.add_stock(stock_abbr, amount)
   guy_print.print_with_dashes(str(amount) + " share(s) of stock " + stock_abbr + " added.")
      

intro()
portfolio = load_portfolio()
while(True):
   action = main_menu(portfolio)
   if(action == main_menu_options.ADD_STOCK):
      add_stock(portfolio)
   elif(action == main_menu_options.SHOW_PORTFOLIO):
      show_portfolio(portfolio)
   elif(action == main_menu_options.EXIT):
      exit()
