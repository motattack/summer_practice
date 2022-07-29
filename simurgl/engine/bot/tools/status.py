import subprocess


def get_basic_info():
    manufacturer = subprocess.check_output(
        '''powershell "Get-CimInstance -ClassName Win32_ComputerSystem | select Manufacturer | ft -hide"''').decode(
        "utf-8", 'ignore').strip()
    time = subprocess.check_output('''powershell "Get-Date -UFormat '%R %d.%m.%Y'"''').decode("utf-8", 'ignore').strip()
    battery = subprocess.check_output(
        '''powershell "Get-CimInstance -ClassName Win32_Battery | Select-Object -ExpandProperty EstimatedChargeRemaining"''').decode(
        "utf-8", 'ignore').strip()
    user = subprocess.check_output("powershell $env:UserName").decode("utf-8", 'ignore').strip()

    return \
        f"""[{manufacturer}]
Пользователь {user},
заряд {battery}%,
системное время {time}"""


def get_all_info():
    info = subprocess.check_output("systeminfo").decode("utf-8", 'ignore').strip()
    return info
