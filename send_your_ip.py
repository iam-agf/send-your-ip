import subprocess
import re
import requests
import time
# Gets the ip address from bash
get_public_ip = subprocess.Popen("curl ifconfig.co", shell = True, stdout = subprocess.PIPE)
public_ip = get_public_ip.stdout.read().decode('utf-8')
public_ip = str(public_ip)
public_ip = [ip for ip in re.findall(r'[0-9]+(?:\.[0-9]+){3}',public_ip)][0]

# Processing IPs from output in bash
get_ip = subprocess.Popen("ip addr show", shell = True, stdout = subprocess.PIPE)
ip_addr_show = get_ip.stdout.read().decode("utf-8")
ip_addr_show = str(ip_addr_show)
filtering_address = [ip for ip in re.findall(r'[0-9]+(?:\.[0-9]+){3}',ip_addr_show)]
filtering_address = list(filter(lambda x: x!='127.0.0.1',filtering_address))
possible_addresses = '\n'.join(filtering_address)

# Processing Linux distribution from the output in bash
get_dist = subprocess.Popen("lsb_release -d", shell = True, stdout = subprocess.PIPE)
distro = get_dist.stdout.read().decode('utf-8')
distro = str(distro)
distro_name = distro.split(':')[1][1:-1]

# Output message to restart
text_model = f"""Hello!\n
You're using the Linux distribution "{distro_name}" in the public IP {public_ip}\n\nThe subnet IPs your device have are:\n{possible_addresses}.
"""

# Runs a basic telegram bot
token = "" # Your Telegram token. You obtain one from the Botfather
user = "" # Your user token. You can obtain it sending a message to the @JsonDumpBot
mail = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={user}&text={text_model}"

time.sleep(1)

send_message = requests.get(mail)
print(send_message.status_code)
time.sleep(1)
if send_message.status_code==200:
    exit()
else:
    print("Message_not_sent")
    raise
