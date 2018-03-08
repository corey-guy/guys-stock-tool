import utilities.guy_print as guy_print


def add_stock(portfolio):
   guy_print.print_with_dashes("What stock would you like to add? Please use ticker letters. Example: MSFT")
   stock_abbr = raw_input()
   guy_print.print_with_dashes("How much of that stock would you like to add? Numbers only, please.")
   amount  = input()
   portfolio.add_stock(stock_abbr, amount)
   guy_print.print_with_dashes(str(amount) + " share(s) of stock " + stock_abbr + " added.")

