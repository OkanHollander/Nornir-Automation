from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def test_task(task):
    int_result = task.run(task=send_command, command="show version")
    struc_output = task.host['facts'] = int_result.scrapli_response.textfsm_parse_output()
    print(struc_output)

result = nr.run(task=test_task)
# print_result(result)