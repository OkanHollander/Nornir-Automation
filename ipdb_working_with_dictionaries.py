from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")


def pull_ospf_info(task):
    ospf_output = task.run(task=send_command, command="show ip ospf neigh")
    task.host['facts'] = ospf_output.scrapli_response.genie_parse_output()
    neighbors = task.host["facts"]["interfaces"]
    for key in neighbors:
        state = neighbors[key]['neighbors']
        for i, v in state.items():
            rprint(f"{task.host} neighbor {i} has state: {v['state']}")

result = nr.run(task=pull_ospf_info)
# print_result(result)
# ipdb.set_trace()
