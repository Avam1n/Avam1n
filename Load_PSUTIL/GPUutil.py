from User_PSUTIL.User import NAME
from Pid_PSUTIL.pid import PID
from exe_PSUTIL.proc import EXE
import psutil
import datetime


# def iter_exe(exe):
#     exe = EXE()
#     iter = list(exe.load_exe())
#     for i in iter:
#         print(iter)


# EXE.load_exe([])


# name = NAME()
# NAME.load_name([])
def iter_pid(pid):
    pid = PID([])
    a = PID.pid_list
    PID.load_pid([])
    print(a[1])


a = iter_pid([])


def disp():
    table_str = f"+{'-' * 8}+{'-' * 14}+{'-' * 55}+\n"
    table_str += "|{:^8}|{:^14}|{:^55}|\n".format('PID', 'Username', "Command's")
    table_str += f"+{'-' * 8}+{'-' * 14}+{'-' * 55}+\n"
    table_str += "|{:^8}|{:^14}|{:^55}|\n".format(f'{111}', f'{2222}', f'{333}')
    table_str += f"+{'_' * 8}+{'_' * 14}+{'_' * 55}+\n"
    print(table_str)


# def time():
#     while True:
#         disp(time(5))


if __name__ == '__main__':
    disp()
    # time()
