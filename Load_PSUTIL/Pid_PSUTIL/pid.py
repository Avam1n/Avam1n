import psutil


class PID:

    def create_pid(self):
        self.pid = psutil.process_iter()

    def load_pid(self):
        for i in psutil.process_iter(['pid']):
            print(i.info.get('pid'))


if __name__ == '__main__':
    p = PID()
    p.load_pid()
