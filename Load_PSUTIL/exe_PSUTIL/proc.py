import psutil


class EXE:

    def create_exe(self):
        self.exe = psutil.Process.exe()

    def load_exe(self):
        for i in psutil.process_iter(['exe']):
            print(i.info.get('exe'))


if __name__ == '__main__':
    e = EXE()
    e.load_exe()
