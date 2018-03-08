import utilities.guy_print as guy_print
import portfolio_modules.portfolio as p

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
