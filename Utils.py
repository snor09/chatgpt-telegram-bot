import datetime
import os
import platform

def saveLog(query):
    print(f"Saving log id: {query.id}")
    today_date = datetime.datetime.today()
    if platform.system() == "Windows":
        file_name = os.path.join(os.getcwd(), f"logs\\{today_date.day}-{today_date.month}-{today_date.year}.txt")
    else:
        file_name = os.path.join(os.getcwd(), f"logs/{today_date.day}-{today_date.month}-{today_date.year}.txt")

    logs_file = open(file_name, "a+")

    time = datetime.datetime.fromtimestamp(query.date).strftime("%H:%M:%S")
    logs_file.write(f"\nid: {query.from_user.id}\nfirst_name: {query.from_user.first_name}\nusername: {query.from_user.username}\ntime: {time}\nquery:\n\t{query.text}\n\n")
    logs_file.read()