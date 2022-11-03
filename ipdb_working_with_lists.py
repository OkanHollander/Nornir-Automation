from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import ipdb
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def pull_structured_data(task):
    interface_result = task.run(task=send_command, command="show ip int")
    task.host["facts"] = interface_result.scrapli_response.genie_parse_output()
    ipv4 = task.host['facts']['FastEthernet0/0']['ip_route_cache_flags']
    for i in ipv4:
        if i == 'CEF':
            rprint(f"{task.host} has CEF enabled")

result = nr.run(task=pull_structured_data)
# print_result(result)
# ipdb.set_trace()