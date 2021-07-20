import pagehandler


def page_handler_functions():
    pagehandler.open_google("https://www.google.com/")
    pagehandler.agree_terms()
    pagehandler.navigate_to_yahoo_finance()
    pagehandler.click_link_to_yahoo()
    pagehandler.agree_yahoo_terms()
    pagehandler.choose_topic("NIO") #Write here your topic
    pagehandler.current_tesla_price()
    pagehandler.close_browser()
