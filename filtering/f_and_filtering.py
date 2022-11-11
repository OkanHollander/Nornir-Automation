from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir.core.filter import F
# import ipdb

nr = InitNornir(config_file="config.yaml")

def test_task(task):
    int_output = task.run(task=send_command, command="show version")
    task.host["facts"] = int_output.scrapli_response.genie_parse_output()
    output = task.host["facts"]["version"]["uptime"]
    print(f"The uptime of device {task.host} is {output}")

filter_device = nr.filter(F(region="east") & F(country="usa"))
result = filter_device.run(task= test_task)
# ipdb.set_trace()