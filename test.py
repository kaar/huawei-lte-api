from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection
import json

# with Connection('http://192.168.8.1/') as connection: For limited access, I have valid credentials no need for limited access
with Connection('http://admin:admin@192.168.8.1/') as connection:
    client = Client(connection) # This just simplifies access to separate API groups, you can use device = Device(connection) if you want

    print(json.dumps(client.device.signal(), indent=2))  # Can be accessed without authorization
    print(json.dumps(client.device.information(), indent=2))  # Needs valid authorization, will throw exception if invalid credentials are passed in URL
