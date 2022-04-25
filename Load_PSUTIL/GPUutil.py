from Pid_PSUTIL.pid import PID
from exe_PSUTIL.proc import EXE
import psutil
import datetime


def disp(func):
    def table():
        template = "{count}\n"
        template += "|" + str(func()) + "|\n"
        print(template)
        print()

    return table


@disp
def pid_create():
    pid_info = PID()
    pid_info.show_info()



# def time():
#     while True:
#         disp(time(5))


if __name__ == '__main__':
    pid_create()
    # time()
