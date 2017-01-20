import threading
from controller import Controller
from reader import Reader

c = Controller()
r = Reader()
threading.Thread(target=c.start).start()
threading.Thread(target=r.get_distance).start()

