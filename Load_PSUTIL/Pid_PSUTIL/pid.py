import psutil


class PID:
    pid_info = {}
    pid_list = []
    name_list = []
    pid_dict = {}
    pid_template = "{pid}\n"

    def get_info(self):
        self.pid_info.update(pid=[pid for pid in psutil.process_iter(['pid'])])

    def _load_pid(self):
        # self.pid_template += "PID\n"
        # for i in range(len(self.pid_info["pid"])):
        #     self.pid_template += "{pid[" + str(i) + "]}\n\n"
        for i in psutil.process_iter():
            pid = PID.pid_list.append(i.pid)
            name = PID.name_list.append(str(i.name()))

    def show_info(self):
        self._load_pid()
        self.pid_dict = dict(zip(self.pid_list, self.name_list))
        print(self.pid_dict)


if __name__ == '__main__':
    p = PID()
    p.get_info()
    p.show_info()
