from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def random_task(task):
    task.run(task=send_config, config=f"ntp server {task.host['ntp_server']}")
    
results = nr.run(task=random_task)
print_result(results)
