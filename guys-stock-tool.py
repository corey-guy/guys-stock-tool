import utilities.guy_print as guy_print
import portfolio as p

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
         print "Sorry, try choosing an option again. Valid options are \"1\" and \"2\""
    
   
intro()
portfolio = load_portfolio()
print portfolio.name

