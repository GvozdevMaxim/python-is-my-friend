class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __len__(self):
        a = self.clock1.hours * 3600 + self.clock1.minutes * 60 + self.clock1.seconds
        b = self.clock2.hours * 3600 + self.clock2.minutes * 60 + self.clock2.seconds
        c = a - b if (a - b) >= 0 else 0
        return c

    def __str__(self):
        res = f"{self.clock1.hours - self.clock2.hours:02}: {self.clock1.minutes - self.clock2.minutes:02}: {self.clock1.seconds - self.clock2.seconds:02}"
        if res.count('-') > 0:
            return "00: 00: 00"
        return res


class Clock:
    def __init__(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def get_time(self):
        res = self.hours * 3600 + self.minutes * 60 + self.seconds
        return res


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)  # 01: 30: 00
len_dt = len(dt)  # 5400
print(len_dt)
