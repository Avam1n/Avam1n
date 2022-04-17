import psutil


class NAME:
    iter = []
    list = "{name}\n"

    def create_name(self):
        self.name = psutil.process_iter()

    def load_name(self):
        for i in psutil.process_iter():
            self.iter.append(i)


if __name__ == '__main__':
    n = NAME()
    n.load_name()
    print(n.iter)
