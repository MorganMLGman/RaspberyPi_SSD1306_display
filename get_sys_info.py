from sys import platform
from platform import system
import sys
import time

def check_system_type(expected: str) -> bool:
    if system() == expected:
        return True
    else:
        return False;

def get_time() -> str:
    cur_time = time.localtime(time.time())

    ret = f"""{cur_time.tm_mday if (cur_time.tm_mday > 9) else f"0{cur_time.tm_mday}"}/{cur_time.tm_mon if (cur_time.tm_mon > 9) else f"0{cur_time.tm_mon}"}/{cur_time.tm_year} \
{cur_time.tm_hour if (cur_time.tm_hour > 9) else f"0{cur_time.tm_hour}"}:{cur_time.tm_min if (cur_time.tm_min > 9) else f"0{cur_time.tm_min}"}:\
{cur_time.tm_sec if (cur_time.tm_sec > 9) else f"0{cur_time.tm_sec}"}"""

    return ret