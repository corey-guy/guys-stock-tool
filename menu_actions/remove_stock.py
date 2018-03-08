import utilities.guy_print as guy_print

def remove_stock(portfolio):
   guy_print.print_with_dashes("What stock would you like to remove? Please choose one listed above.")
   stock_abbr = raw_input()
   guy_print.print_with_dashes("How much of that stock would you like to remove? Numbers only, please.")
   amount = input()
   status = portfolio.remove_stock(stock_abbr, amount)
   if(status == -1):
      guy_print.print_with_dashes("Error removing stock, please make sure you use a valid abbreviation.")
   else:
      guy_print.print_with_dashes(str(amount) + " share(s) of stock " + stock_abbr + " removed. You now have " + str(portfolio.get_stock_amount(stock_abbr)) + " share(s) left.")


