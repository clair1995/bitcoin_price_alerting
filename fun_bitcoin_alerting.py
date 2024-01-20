# bitcoin price alerting function

# needs 3 elements:
    # notification object
    # bitcoin price web-scraped
    # treshold for the notification

# if price is above the treshold, print the message

def toast_notification_bitcoin(notification, bitcoin_price, treshold):
    
    import datetime
    
    # set the condition: when the pop-up has to appear?
    if bitcoin_price < treshold:
        
        # set the time when the toast notification appears
        now = datetime.datetime.now()
        year = '{:02d}'.format(now.year)
        month = '{:02d}'.format(now.month)
        day = '{:02d}'.format(now.day)
        hour = '{:02d}'.format(now.hour)
        minute = '{:02d}'.format(now.minute)
        day_month_year = '{}-{}-{} \t {}:{}'.format(year, month, day, hour, minute)
        time   = "\nUpdated time: " + day_month_year 
        # write the price
        result = 'TIME TO BUY!\n' + "Bitcoin Price: " + str(bitcoin_price)
        notification.update(result, time)
        
        # Show the notification
        notification.show()
        
        return time