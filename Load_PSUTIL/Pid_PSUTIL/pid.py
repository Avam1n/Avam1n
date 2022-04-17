import psutil


class PID:
    pid_list = []
    name_list = []
    pid_dict = {}

    def _load_pid(self):
        for i in psutil.process_iter():
            pid = PID.pid_list.append(i.pid)
            name = PID.name_list.append(str(i.name()))

    def show_info(self):
        self._load_pid()
        self.pid_dict = dict(zip(self.pid_list, self.name_list))

        print(self.pid_dict)


if __name__ == '__main__':
    p = PID()
    p.show_info()
