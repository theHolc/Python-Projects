import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 22):
        print("working hours...")
        with open(hosts_path, "r+") as f:
            content = f.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    f.write(redirect + "       " + website + "\n")
    else:
        with open(hosts_path, "r+") as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    f.write(line)
            f.truncate()
        print("fun hours!")
    time.sleep(5)

