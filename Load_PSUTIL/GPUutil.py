from User_PSUTIL.User import NAME
from Pid_PSUTIL.pid import PID
from exe_PSUTIL.proc import EXE
import psutil
import datetime

exe = EXE()

name = NAME()

pid = PID()


def disp():
    table_str = f"|{'-' * 8}|{'-' * 14}|{'-' * 55}|\n"
    table_str += "|{:^8}|{:^14}|{:^55}|\n".format('PID', 'Username', "Command's")
    table_str += f"|{'-' * 8}|{'-' * 14}|{'-' * 55}|\n"
    table_str += "|{:^8}|{:^14}|{:^55}|\n".format(f'{PID.load_pid()}', f'{NAME.load_name()}', f'{EXE.load_exe()}')
    table_str += f"|{'-' * 8}|{'-' * 14}|{'-' * 55}|\n"
    table_str += "|{:^8}|{:^14}|{:^55}|\n".format(f'{PID.load_pid()}', f'{NAME.load_name()}', f'{EXE.load_exe()}')
    table_str += f"|{'-' * 8}|{'-' * 14}|{'-' * 55}|\n"
    table_str += "|{:^8}|{:^14}|{:^55}|\n".format(f'{PID.load_pid()}', f'{NAME.load_name()}', f'{EXE.load_exe()}')
    table_str += f"|{'_' * 8}|{'_' * 14}|{'_' * 55}|\n"
    print(table_str)


# def time():
#     while True:
#         disp(time(5))


if __name__ == '__main__':
    disp()
    # time()
