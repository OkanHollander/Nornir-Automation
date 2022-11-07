from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.functions import print_structured_result
from rich import print as rprint
from tqdm import tqdm
# import ipdb

nr = InitNornir(config_file="config.yaml")

def random_task(task, progress_bar):
    progress_bar.update()
    int_output = task.run(task=send_command, command="show ip int brief")
    task.host["facts"] = int_output.scrapli_response.genie_parse_output()
    interface = task.host["facts"]["interface"]
    for k, v in interface.items():      
        if v['status'] != "administratively down":
            rprint(f"{task.host} interface: {k} has ip address: {v['ip_address']}")

with tqdm(total=len(nr.inventory.hosts)) as progress_bar:    
    result = nr.run(task=random_task, progress_bar=progress_bar)
# print_structured_result(result, parser="genie")
# print_result(result)
# ipdb.set_trace()