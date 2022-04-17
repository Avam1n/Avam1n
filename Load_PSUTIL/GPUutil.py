from Pid_PSUTIL.pid import PID
from exe_PSUTIL.proc import EXE
import psutil
import datetime


def disp():
    template = ""
    pid_info = PID()
    pid_info.show_info()
    for key, value in pid_info.pid_dict:
        template += "|{:^8}|{:^14}|{:^55}|\n".format(f'{key}', f'{"value"}', f'{""}')
    print(key, value)

    exe_info = EXE()
    exe_info.show_info()

    table_str = f"+{'-' * 8}+{'-' * 14}+{'-' * 55}+\n"
    table_str += "|{:^8}|{:^14}|{:^55}|\n".format('PID', 'Username', "Command's")
    table_str += f"+{'-' * 8}+{'-' * 14}+{'-' * 55}+\n"
    table_str += "|{:^8}|{:^14}|{:^55}|\n".format(f'{template}', f'{2222}', f'{3333}')
    table_str += f"+{'_' * 8}+{'_' * 14}+{'_' * 55}+\n"
    print(table_str)


# def time():
#     while True:
#         disp(time(5))


if __name__ == '__main__':
    disp()
    # time()
