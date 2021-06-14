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
    return f"CPU {round((cpu * 100), 1)}%"

def get_ip_address() -> str:
    cmd = "hostname -I | cut -d ' ' -f 1"
    ip = str(check_output(cmd, shell = True))
    ip = ip[2:-3]
    return f"IP {ip}"

def get_ram_usage() -> str:
    cmd = """free -m | awk 'NR==2{printf "%s", $2}'"""
    ram_total = str(check_output(cmd, shell = True))
    cmd = """free -m | awk 'NR==2{printf "%s", $3}'"""
    ram_used = str(check_output(cmd, shell = True))

    ram_used = int(ram_used.replace("b", "").replace("'", ""))
    ram_total = int(ram_total.replace("b", "").replace("'", ""))

    return f"RAM {round((ram_used/ram_total)*100, 1)}%"

def get_disk_usage() -> str:
    cmd = """df | awk '$NF=="/"{printf "%d", $3}'"""
    disk_usage = str(check_output(cmd, shell = True))
    cmd = """df | awk '$NF=="/"{printf "%d", $2}'"""
    disk_total = str(check_output(cmd, shell = True))

    disk_usage = int(disk_usage.replace("b", "").replace("'", ""))
    disk_total = int(disk_total.replace("b", "").replace("'", ""))

    return f"DISK {round((disk_usage/disk_total)*100, 1)}%"

def get_temperature() ->str:
    cmd = """vcgencmd measure_temp | cut -d '=' -f 2 | cut -d "'" -f 1"""
    temp = str(check_output(cmd, shell = True))
    temp = temp[2:-3]
    
    return f"TEMP {temp}°C"

def get_arm_freq() -> str:
    cmd = """vcgencmd measure_clock arm | cut -d '=' -f 2"""
    freq = str(check_output(cmd, shell = True))[2:-3]
    freq = float(freq)/1000000
    
    return f"{round(freq)} MHz"