from netmiko import ConnectHandler


cisco_username = input("Enter Username: ")
cisco_password = input("Enter Password: ")

R1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.177.101',
    'username': cisco_username,
    'password': cisco_password,
}

R2 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.177.102',
    'username': cisco_username,
    'password': cisco_password,
}

R3 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.177.103',
    'username': cisco_username,
    'password': cisco_password,
}

my_routers = [R1, R2, R3]

for router in my_routers:
    net_connect = ConnectHandler(**router)
    output = net_connect.send_config_from_file("cisco_commands.txt")
    print("!#****************************\n")
    print(output)
