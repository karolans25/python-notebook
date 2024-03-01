# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def __str__(self):
        mins = str(self.minutes) if self.minutes >= 10 else '0'+str(self.minutes)
        secs = str(self.seconds) if self.seconds >= 10 else '0'+str(self.seconds)
        return f"{mins}:{secs}"

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0

if __name__ == '__main__':
    watch = Stopwatch()
    for i in range(180):
        print(watch)
        watch.tick()
