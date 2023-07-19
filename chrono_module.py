import time

""" return True  when not finished
"""

class Chrono:
    def __init__(self, delta):
        self.delta = delta
        self.t0 = time.time()  # top in sec

    def delta_t(self):
        return (time.time() - self.t0 - self.delta) < 0
        # return True when delta not finished

    def reset(self):
        self.t0 = time.time()


if __name__ == "__main__":
    c = Chrono(10)
    print(c.delta)

    while c.delta_t():
        # if c.delta_t<0 duration not finished
        v = 2 / 3
    print(c.delta_t())
