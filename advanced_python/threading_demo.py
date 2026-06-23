import threading

def attendance():
    print("Attendance Processing")

def certificate():
    print("Certificate Generation")

t1 = threading.Thread(target=attendance)
t2 = threading.Thread(target=certificate)

t1.start()
t2.start()