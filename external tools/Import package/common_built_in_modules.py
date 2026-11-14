# Date and time 

import datetime 

today = datetime.date.today()
print(today) # 14/11/2026

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}

json_string = json.dumps(data)

print(json_string)