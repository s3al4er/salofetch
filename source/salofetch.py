import platform
import pyfiglet
import psutil
import GPUtil
import cpuinfo

def get_system_info():
    system_info = {}
    system_info['Operating System'] = platform.system() + ' ' + platform.release()

    cpu_info = cpuinfo.get_cpu_info()
    system_info['Processor'] = f"{cpu_info['brand_raw']}"

    system_info['RAM'] = round(psutil.virtual_memory().total / (1024 ** 3), 2)

    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu_name = gpus[0].name
            system_info['Graphics Card'] = gpu_name
        else:
            system_info['Graphics Card'] = 'N/A'
    except Exception as e:
        system_info['Graphics Card'] = f'Error: {str(e)}'

    return system_info

def display_system_info(system_info):
    os_name = system_info['Operating System']
    styled_text = pyfiglet.figlet_format(os_name, font="slant")
    print(styled_text)
    for key, value in system_info.items():
        print(f"{key}: {value}")

def main():
    system_info = get_system_info()
    display_system_info(system_info)

if __name__ == "__main__":
    main()
