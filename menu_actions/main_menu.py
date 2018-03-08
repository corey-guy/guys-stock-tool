import utilities.guy_print as guy_print
import menu_actions.main_menu_options as main_menu_options

def main_menu(portfolio):
   option_is_valid = False
   guy_print.print_with_dashes("What do you want to do with " + portfolio.name + "?\n1.Add Stock\n2.Remove Stock\n3.Show Portfolio\nOR\n4.Exit Program")
   while(option_is_valid != True):
      input = raw_input()
      if(input == "1"):
         return main_menu_options.ADD_STOCK
      elif(input == "2"):
         return main_menu_options.REMOVE_STOCK
      elif(input == "3"):
         return main_menu_options.SHOW_PORTFOLIO
      elif(input == "4"):
         return main_menu_options.EXIT
      else:
         guy_print.print_retry_message()

