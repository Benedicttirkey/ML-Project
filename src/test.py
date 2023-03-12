import logging
import os
from datetime import date, datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)


CD=f"{datetime.now().strftime('%m_%d_%Y')}"
ad=LOG_FILE[0:10]
print("date from log file",ad)
print("Current date",CD)

if ad==CD:
    print("valla!!")
else:
    print("nah!!")

