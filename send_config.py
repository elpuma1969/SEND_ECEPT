from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

u1 = input('Enter your SSH username: ')
password1 = getpass()


class MyNetmiko:
    def __init__(self, device_type, host, username, password, read_timeout=500):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password
        self.read_timeout = read_timeout

    def connect(self):
        connection = ConnectHandler(device_type=self.device_type, host=self.host, username=self.username,
                                    password=self.password, read_timeout=self.read_timeout)
        return connection


def show_cmd():
    with open('STEVEN.txt') as f:
        commands_list = f.read().splitlines()

    with open('jose.txt') as f:
        device_list = f.read().splitlines()

    for device in device_list:
        print('Connecting to device:', device)
        try:
            ios_device = {
                'device_type': 'cisco_ios',
                'ip': device,
                'username': u1,
                'password': password1,
                'secret': password1,
                'port': 22,
                'verbose': False,
            }

            net_conn = ConnectHandler(**ios_device)
            print('Entering enable mode...')
            net_conn.enable()

            output = net_conn.send_config_set(commands_list)
            print(output)

            prompt = net_conn.find_prompt()
            hostname = prompt[0:-1]

            now = datetime.now()
            year = now.year
            month = now.month
            day = now.day

            filename = f'C:\\Users\\joserodriguez\\Desktop\\DSNY\\MASTER_1\\Sent_commands\\' \
                       f'{hostname}_{year}-{month}-{day}_.txt'

            with open(filename, 'w') as final:
                final.write(output)
                +0
                print(f'Backup of {hostname} completed successfully')
                print('#' * 30)

            print('Closing connection')
            net_conn.disconnect()
        except Exception as e:
            print(f'An error occurred while processing device {device}: {str(e)}')
            print('#' * 30)


show_cmd()




