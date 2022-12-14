from nornir import InitNornir
from nornir_scrapli.tasks import netconf_edit_config
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file

nr = InitNornir(config_file="config.yaml")

def configure_ospf(task):
    template_to_load = task.run(task=template_file, template="ospf.j2", path="templates")
    configuration = template_to_load.result
    task.run(task=netconf_edit_config, target="running", config=configuration)

result = nr.run(task=configure_ospf)
print_result(result)