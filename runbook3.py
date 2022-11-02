from nornir import InitNornir
# from nornir_scrapli.tasks import send_command
from nornir_scrapli.tasks import send_commands
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

command_list = ['show ip int brief', 'show version', 'show ip route']
def show_command_test(task):
    for cmd in command_list:
        task.run(task=send_commands, commands=command_list)


results = nr.run(show_command_test)
print_result(results)
