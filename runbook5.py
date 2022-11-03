from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def show_command_test(task):
    task.run(task=netmiko_send_command, command_string="show ip int brief")


result = nr.run(task=show_command_test)
print_result(result)
