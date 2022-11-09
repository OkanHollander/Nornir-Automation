from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get
from nornir_utils.plugins.functions import print_result
import xmltodict
from pprint import pprint
import ipdb

nr = InitNornir(config_file="config.yaml")

def get_yang(task):
    result = task.run(task=netconf_get, filter_type="xpath", filter_="interfaces-state//statistics[in-unicast-pkts > 0]")
    output = result.result
    dict_result = xmltodict.parse(output)
    task.host["facts"] = dict_result

result = nr.run(task=get_yang)
# print_result(result)
ipdb.set_trace()