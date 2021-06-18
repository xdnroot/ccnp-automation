import paramiko
import time

ip_address = "10.1.4.100"
username = "cisco"
password = "cisco123"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password, look_for_keys=False)

print ("Success login to {0}".format(ip_address))
conn = ssh_client.invoke_shell()

conn.send("terminal length 0\n")
conn.send("show run\n")
time.sleep(3)

output = conn.recv(65535).decode("utf-8")

output_file=open("{0}.cfg".format(ip_address), "w")
output_file.write(output)
output_file.close()

print("Config in {0} saved!!".format(ip_address))

ssh_client.close()