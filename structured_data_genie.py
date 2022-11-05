from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def test_tak(task):
    interface_output = task.run(task=send_command, command="show interfaces")
    structured_output = interface_output.scrapli_response.genie_parse_output()
    print(f"{task.host}: {structured_output}")

result = nr.run(task=test_tak)
# print_result(result)