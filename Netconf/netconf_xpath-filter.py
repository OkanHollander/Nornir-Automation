from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get
from nornir_scrapli.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

# def get_yang(task):
#     task.run(task=netconf_get_config,
#              source="running",
#              filter_type="xpath",
#              filter_="/native")

def get_yang(task):
    task.run(task=netconf_get, 
             filter_type="xpath", 
             filter_="/native/interface/GigabitEthernet[name = 2]")
             #filter_="interfaces-state//statistics[in-unicast-pkts > 0]")   # filter_="//filter" for recursive lookup

results = nr.run(task=get_yang)   
print_result(results)