class Track:
    def __init__(self, start_x, start_y):
        self.start_x = self.start_y = None
        if type(self.start_x) and type(self.start_y) in (int, float):
            self.start_x = start_x
            self.start_y = start_y

    def add_track(self, tr):
        self.way.append(tr)

    def get_tracks(self):
        return tuple(self.way)
class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = self.to_y = self.max_speed = None
        if type(self.to_x) and type(self.to_y) and type(self.max_speed) in (int, float):
            self.to_x = to_x
            self.to_y = to_y
            self.max_speed = max_speed


track1, track2 = Track(0, 0), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2