class Clock:

    def __init__(self, hour=0, minute=0):
        self.time = (hour % 24, minute % 60)

    @classmethod
    def at(cls, hour=0, minute=0):
        return cls(hour, minute)
    
    def __add__(self, add_time):
        hour, minute = divmod(add_time, 60)
        total_minutes = self.time[1] + minute
        extra_hour, final_minute = divmod(total_minutes, 60)
        total_hours = (self.time[0] + extra_hour + hour) % 24
        return Clock.at(total_hours, final_minute)
    
    def __sub__(self, sub_time):
        hour, minute = divmod(sub_time, 60)
        hour = ((self.time[0] - hour) - (1 if self.time[1] < minute else 0)) % 24
        minute = self.time[1] - minute
        return Clock.at(hour, minute)
    
    def __str__(self):
        return ":".join(f'{time:02d}' for time in self.time)
    
    def __eq__(self, other):
        if not isinstance(other, Clock):
            return NotImplemented
        return str(self) == str(other)
    
    def __ne__(self, other):
        if not isinstance(other, Clock):
            return NotImplemented
        return not str(self) == str(other)
    
