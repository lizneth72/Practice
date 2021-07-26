from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_netmiko import netmiko_send_config
from nornir_utils.plugins.functions import print_result

# Example 1: Sending commands.
nr = InitNornir()
result = nr.run(task=netmiko_send_command,
                command_string="show ip interface brief")
print_result(result)


# Example 2: Sending configs from list.
nr = InitNornir()
result = nr.run(task=netmiko_send_config,
                config_commands=["no ip http server",
                                 "no ip http secure-server"])
print_result(result)


# Example 3: Sending configs from file.
nr = InitNornir()
result = nr.run(task=netmiko_send_config,
                config_file="cisco_commands.txt")
print_result(result)

