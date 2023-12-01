class process_data(object):

    def __init__(self, heartrate, timestamp):
        self._hr = heartrate
        self._time = timestamp

    @property
    def hr(self):
        return self._hr

    @hr.setter
    def x(self, value):
        self._hr = value

    @hr.deleter
    def hr(self):
        del self._hr

    @property
    def time(self):
        return self._time

    @time.setter
    def x(self, value):
        self._time = value

    @time.deleter
    def time(self):
        del self._time