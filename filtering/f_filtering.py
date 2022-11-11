from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_scrapli.functions import print_structured_result
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")

def test_task(task):
    task.run(task=send_command, command="show version")

region = nr.filter(F(region="east"))
result = region.run(task=test_task)
print_structured_result(result, parser="genie")
