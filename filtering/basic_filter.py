from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def test_task(task):
    task.run(task=send_command, command="show ip int brief")


usa_targets = nr.filter(country="usa")

result = usa_targets.run(task=test_task)
print_result(result)