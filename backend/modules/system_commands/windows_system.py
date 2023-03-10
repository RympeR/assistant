import os
import sys
import subprocess


class WindowsSystem:
    """
    Windows system commands module
        methods:
            shutdown() - shutdown system
            restart() - restart system
            restart_in_time(time) - restart system in time
                args:
                    time: int - time in seconds
            shutdown_in_time(time) - shutdown system in time
                args:
                    time: int - time in seconds
            get_current_user() - get current user
            get_current_user_id() - get current user id
            get_current_user_group() - get current user group
            get_current_user_group_id() - get current user group id
            get_current_user_home() - get current user home directory
            stop_process_by_name(name) - stop process by name
            stop_system_shutdown() - stop system shutdown
            get_system_datetime() - get system datetime
    """
    @staticmethod
    def shutdown():
        subprocess.call('powershell shutdown /s')

    @staticmethod
    def restart():
        subprocess.call('powershell shutdown /r')

    @staticmethod
    def restart_in_time(time: int):
        subprocess.call(f'powershell shutdown /r /t {time}')

    @staticmethod
    def shutdown_in_time(time: int):
        subprocess.call(f'powershell shutdown /s /t {time}')

    @staticmethod
    def get_current_user():
        return os.getlogin()

    @staticmethod
    def get_current_user_id():
        return os.getuid()

    @staticmethod
    def get_current_user_group():
        return os.getgid()

    @staticmethod
    def get_current_user_group_id():
        return os.getgroups()

    @staticmethod
    def get_current_user_home():
        return os.path.expanduser('~')

    @staticmethod
    def stop_process_by_name(name):
        subprocess.call(f'powershell Stop-Process -Name {name}')

    @staticmethod
    def stop_system_shutdown():
        subprocess.call(f'powershell shutdown /a')

    @staticmethod
    def get_system_datetime():
        return subprocess.check_output('powershell Get-Date', shell=True).decode('windows-1251')


# value = subprocess.run('powershell ls')
# value = subprocess.call('powershell ls')
# proc = subprocess.Popen('powershell ls', stdout=subprocess.PIPE)
# print(dir(value))
# print(proc.stdout.read().decode('windows-1251'))
# print(value.stderr)
