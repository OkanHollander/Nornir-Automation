from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir.core.filter import F
# import ipdb

nr = InitNornir(config_file="config.yaml")

def test_task(task):
    sh_int = task.run(task=send_command, command="show interfaces")
    filter_output = task.host["facts"] = sh_int.scrapli_response.genie_parse_output()
    for interface in filter_output:
        ipv4 = filter_output[interface]["ipv4"]
        for v in ipv4.values():
            print(f"{task.host}'s interface {interface} has ip: {v['ip']}/{v['prefix_length']}")
        

filtered = nr.filter(~F(country="germany") & F(region="east"))
result = filtered.run(task=test_task)
# ipdb.set_trace()