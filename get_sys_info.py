from sys import platform
from platform import system
from subprocess import check_output
import time

def check_system_type(expected: str) -> bool:
    if system() == expected:
        return True
    else:
        return False;

def get_time() -> str:
    cur_time = time.localtime(time.time())

    ret = \
f"""{cur_time.tm_hour if (cur_time.tm_hour > 9) else f"0{cur_time.tm_hour}"}:{cur_time.tm_min if (cur_time.tm_min > 9) else f"0{cur_time.tm_min}"}:\
{cur_time.tm_sec if (cur_time.tm_sec > 9) else f"0{cur_time.tm_sec}"}"""

    return ret

def get_cpu_usage() -> str:
    cmd = "top -bn1 | grep load | cut -d ',' -f 3 | cut -d ':' -f 2"
    cpu = check_output(cmd, shell = True)
    cpu.strip()
    cpu = float(cpu)
    cpu /= 4.0
    return str(f"CPU: {round((cpu * 100), 1)}%")