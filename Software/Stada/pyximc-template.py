from ctypes import *
import os
import platform
import sys

# Load library

# use cdecl on unix and stdcall on windows
def ximc_shared_lib():
    if platform.system() == "Linux":
        return CDLL("libximc.so")
    elif platform.system() == "FreeBSD":
        return CDLL("libximc.so")
    elif platform.system() == "Darwin":
        return CDLL("libximc.framework/libximc")
    elif platform.system() == "Windows":
        if sys.version_info[0] == 3 and sys.version_info[0] >= 8:
            return WinDLL("libximc.dll", winmode=RTLD_GLOBAL)
        else:
            return WinDLL("libximc.dll")
    else:
        return None

lib = ximc_shared_lib()

# Common declarations

class Result:
    Ok = 0
    Error = -1
    NotImplemented = -2
    ValueError = -3
    NoDevice = -4


class calibration_t(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('A', c_double),
        ('MicrostepMode', c_uint)
    ]

class device_enumeration_t(LittleEndianStructure):
    pass

class device_network_information_t(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('ipv4', c_uint32),
        ('nodename', c_char * 16),
        ('axis_state', c_uint),
        ('locker_username', c_char * 16),
        ('locker_nodename', c_char * 16),
        ('locked_time', c_ulonglong),
    ]


# Clarify function types

lib.enumerate_devices.restype = POINTER(device_enumeration_t)
lib.get_device_name.restype = c_char_p


# @@GENERATED_CODE@@



# vim: set ft=python
