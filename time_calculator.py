def add_time(current_time, plus_time , day = None ):
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    error = "ERROR: Format error"
    time_dict = {}
    plus_dict = {}
    time = ""

    #------------------------------------------------------ Start ---------------------------------------------
    #----------------------------------------------Check for fomrat errors-------------------------------------
    #Create a list of the elements of the current time ["Hour:minutes","AM/PM"]
    time_list = current_time.split()    
    
    #Make sure hours and minutes are indeed numbers
    try:
        #Separate hours and minutes by the ':' symbol
        time_dict["hour"] = int(time_list[0].split(':')[0])
        time_dict["minutes"] = int(time_list[0].split(':')[1])
        plus_dict["hour"] = int(plus_time.split(':')[0])
        plus_dict["minutes"] = int(plus_time.split(':')[1])
        
    except:
        return error
    
    #Store the AM/PM
    time_dict["meridiem"] = time_list[1]
    
    #Store day value if given
    #Format the day with the first letter as capital letter
    if  day != None: time_dict["day"] = day.lower().title()
    else: time_dict["day"] = ""

    #Check that the minutes are less than 60
    if (time_dict["minutes"] >= 60) or (plus_dict["minutes"] >= 60): return error
    
    #Check that there is a AM/PM indicator
    if time_dict["meridiem"] not in ["AM","PM"]: return error

    #Check if the day is in the days of the week
    if day != None:
        if day not in days: return error
    
    #----------------------------------------------Check for fomrat errors-------------------------------------
    #------------------------------------------------------- End ----------------------------------------------


    #------------------------------------------------------ Start ---------------------------------------------
    #----------------------------------------------------Adding time-------------------------------------------

    ## 1.- Change to 24 hour clock for simplicity
    if time_dict["meridiem"] == "PM": 
        time_dict["hour"] += 12
        time_dict["meridiem"] = None

    ## 2.- Add minutes
    mins = time_dict["minutes"] + plus_dict["minutes"]
    #If the minutes are bigger than 60, we add an hour
    extra_hour = int(mins / 60)
    #We take the module 60 to get the minutes from [0,59]
    time_dict["minutes"] = mins % 60
    
    ## 3.- Add hours
    time_dict["hour"] += (plus_dict["hour"] + extra_hour)
    #Calculate how many days extra have passed from the current time to the added time
    time_dict["n days"] = int(time_dict["hour"]/24)
    #Calculate the current hour of the day
    time_dict["hour"] %= 24

    ## 4.- Return to the 12 hour format
    # if the hour is greater or equal to 12h then it's PM else it's AM
    if (int(time_dict["hour"] / 12) == 0): time_dict["meridiem"] = "AM"
    else: time_dict["meridiem"] = "PM"
    #Caclulate the 12 hour format
    time_dict["hour"] %= 12
    #Replace 0 to 12
    if time_dict["hour"] == 0: time_dict["hour"] = 12

    ## 5.- Convert to string
    time_dict["hour"] = str(time_dict["hour"])
    if time_dict["minutes"] < 10: time_dict["minutes"] = "0" + str(time_dict["minutes"])
    else: time_dict["minutes"] = str(time_dict["minutes"])

    ## 5.A.- Get the day of the week after adding time
    if day != None: 
        #This will return the elapsed days with information on the starting day
        days_elapsed = days.index(time_dict["day"]) + time_dict["n days"]
        #Use the list of days with index 0 to 6 to determine the new current day
        time_dict["day"] = ", " + days[days_elapsed%7]

    ## 6.- Format the output
    #Format if the day is given
    if time_dict["n days"] == 0:
        time = time_dict["hour"] + ":" + time_dict["minutes"] + " " + time_dict["meridiem"] + time_dict["day"] 
    elif time_dict["n days"] == 1:
        time = time_dict["hour"] + ":" + time_dict["minutes"] + " " + time_dict["meridiem"] + time_dict["day"] + " (next day)"
    else:
        time = time_dict["hour"] + ":" + time_dict["minutes"] + " " + time_dict["meridiem"] + time_dict["day"] + " " + str(time_dict["n days"]) + " days later)"

    #----------------------------------------------------Adding time-------------------------------------------
    #------------------------------------------------------- End ----------------------------------------------
    
    
    return time

print(add_time("11:06 PM", "2:02"))