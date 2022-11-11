from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.functions import print_structured_result

nr = InitNornir(config_file="config.yaml")

def test_task(task):
    task.run(task=send_command, command="show version")

result = nr.run(task=test_task)
print_structured_result(result, parser="genie")
