import psutil


class NAME:

    def create_name(self):
        self.name = psutil.process_iter()

    def load_name(self):
        for i in psutil.process_iter(['name']):
            print(i.info.get('name'))


if __name__ == '__main__':
    n = NAME()
    n.load_name()
