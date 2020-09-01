import time

on = True

while True:
    if on == True:
        print("Lights turned on")
        time.sleep(2)
        on = False
    elif on == False:
        print("Lights turned off")
        time.sleep(2)
        on = True
    else:
        print("wtf how did you break it")
        time.sleep(2)
        on = True

