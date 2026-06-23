from multiprocessing import Process

def report(name):
    print("Report:", name)

p1 = Process(target=report,args=("Rahul",))
p2 = Process(target=report,args=("Khushi",))

p1.start()
p2.start()