from netmiko import ConnectHandler


def vlan_run(ip, username, password, vlans):
    try:
        device = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': username,
            'password': password,
            'global_delay_factor': 2,  # Increase global delay factor for slower devices
            'timeout': 30,  # Increase timeout value
            'session_timeout': 60,  # Increase session timeout value
            'fast_cli': False,  # Disable fast_cli mode for better compatibility
        }

        connection = ConnectHandler(**device)
        print(f"Connected to device: {ip}")

        config_commands = []
        for vlan_id, vlan_name in vlans.items():
            command = f"vlan {vlan_id}\nname {vlan_name}"
            config_commands.append(command)

        output = connection.send_config_set(config_commands, cmd_verify=False)
        print(output)

        connection.disconnect()
        print(f"Disconnected from device: {ip}")

    except Exception as e:
        print(f"An error occurred while configuring device {ip}: {str(e)}")


with open('boxes.txt', 'r') as file:
    device_ips = file.read().splitlines()

vlans = {
    '10': 'New_balance',
    '20': 'AirMax',
    '30': 'Yeezy',
}

username = 'puma'
password = 'cisco'

for ip in device_ips:
    vlan_run(ip, username, password, vlans)
