from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint
import ipdb

nr = InitNornir(config_file="config.yaml")

def pull_structured_data(task):
    version_result = task.run(task=send_command, command="show version")
    task.host["facts"] = version_result.scrapli_response.genie_parse_output()
    # rprint(task.host["facts"])
    uptime = task.host["facts"]["version"]["uptime"]
    rprint(f"{task.host} has an uptime of {uptime}")


result = nr.run(pull_structured_data)
# print_result(result)
# nr.inventory.hosts[]
# ipdb.set_trace()