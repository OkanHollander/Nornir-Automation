from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def send_config_test(task):
    task.run(task=netmiko_send_config, config_commands=["no router ospf 1"])

result = nr.run(task=send_config_test)
print_result(result)
