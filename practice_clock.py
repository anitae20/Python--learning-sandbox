import datetime   #python built in clock :)
#accessing the datetime module


date = datetime.date(2025, 1, 2)
print(date)

today = datetime.date.today()
print(today)  # this help directly print the day date 

time =datetime.time(12,30,7)#print the current time (day,minutes,seconds)
print(time)

#today =datetime.time.today()  I did this following a format but I got a traceback
#print(today)

#getting the time now on the system clock
now =datetime.datetime.now()# here we access the datetime module and there is datetime class we have to access 
#here is the output 2026-09-06 13:13:52.320639 we can format the appearance
now = now.strftime("%H:%M:%S %m-%d-%Y")
print(now)

target_datetime = datetime.datetime(2020 ,8 ,2 ,12 ,4 ,8)
current_datetime =datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")