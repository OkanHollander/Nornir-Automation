from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result
from rich import print as rprint
import ipdb

nr = InitNornir(config_file="config.yaml")

def pull_interface_info(task):
    interface_result = task.run(task=send_command, command="show cdp neighbor")
    task.host['facts'] = interface_result.scrapli_response.genie_parse_output()
    index = task.host['facts']['cdp']['index']
    for i in index:
        local_port = index[i]['local_interface']
        remote_device = index[i]['device_id']
        remote_port_id = index[i]['port_id']
        # rprint(f"{task.host} interface: {local_port} has remote device: {remote_device[0:2]} on port: {remote_port_id}")
        config_commands = [f"interface {local_port}", f"description Connected to {remote_device} via its {remote_port_id}"]
        task.run(task=send_configs, configs=config_commands)

result = nr.run(task=pull_interface_info)
print_result(result)

# ipdb.set_trace()