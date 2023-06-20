from netmiko import ConnectHandler

def vlan_run(ip, username, password, vlans):
    try:
        device = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': username,
            'password': password,
        }

        connection = ConnectHandler(**device)
        print(f"Connected to device: {ip}")

        config_commands = []
        for vlan_id, vlan_name in vlans.items():
            command = f"vlan {vlan_id}\nname {vlan_name}"
            config_commands.append(command)

        output = connection.send_config_set(config_commands)
        print(output)

        connection.disconnect()
        print(f"Disconnected from device: {ip}")

    except Exception as e:
        print(f"An error occurred while configuring device {ip}: {str(e)}")

with open('device_ips.txt', 'r') as file:
    device_ips = file.read().splitlines()

vlans = {
    '10': 'VLAN10',
    '20': 'VLAN20',
    '30': 'VLAN30',
}

username = 'your_username'
password = 'your_password'

for ip in device_ips:
    vlan_run(ip, username, password, vlans)
