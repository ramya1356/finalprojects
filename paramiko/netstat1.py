import paramiko
import pandas as pd
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="10.0.2.15",username="ramya",password="ramya")
stdin,stdout,stderr=ssh.exec_command("netstat --listening|less")
# print(stdout)
# print(stdin)
# print(stderr)(stdout)
df=pd.DataFrame(stdout)
print(df)
