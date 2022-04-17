import psutil


class PID:
    pid_list = {}
    template = "{count}\n"

    def create_pid(self):
        self.pid_list.update(count=psutil.cpu_count())
        self.pid_list.update(for pid in psutil.process_iter([]))

    def _load_pid(self):
        self.template += "Pid\n"
        for i in range(len(self.pid_list)):
            self.template += "{Pid[" + str(i) + "]}\n"

    def show_info(self):
        self._load_pid()
        print(self.template)
        print(self.pid_list)
        print(psutil.process_iter(['pid']))


if __name__ == '__main__':
    p = PID()
    p.show_info()
