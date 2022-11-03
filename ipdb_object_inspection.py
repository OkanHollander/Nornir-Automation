from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def pull_structured_data(task):
    task.run(task=send_command, command="show version")


result = nr.run(pull_structured_data)
print_result(result)
