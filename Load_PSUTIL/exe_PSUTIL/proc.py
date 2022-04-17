import psutil


class EXE:
    exe_list = []

    def _load_exe(self):
        for i in psutil.process_iter(['exe']):
            self.exe_list.append(i.info.get('exe'))

    def show_info(self):
        self._load_exe()

        print(self.exe_list)


if __name__ == '__main__':
    e = EXE()
    e.show_info()
