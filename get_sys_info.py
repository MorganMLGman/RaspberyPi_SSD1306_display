from sys import platform
from platform import system
import sys
import time

def check_system_type(expected: str) -> bool:
    if system() == expected:
        return True
    else:
        return False;

print(check_system_type("Linux"))