#!/usr/bin/env python3

import json

# Raw JSON string (notice the triple quotes to handle a multi-line string)
api_payload = """
{
    "status": "success",
    "datacenter": "us-east-1",
    "hosts": [
        {"name": "web-01", "role": "frontend"},
        {"name": "db-01", "role": "backend"}
    ]
}
"""

parsed_data = json.loads(api_payload)

print(f"Datacenter Location: {parsed_data['datacenter']}")

for server in parsed_data['hosts']:
    print(f"The host {server['name']} is a {server['role']} server.")