#!/usr/bin/env python3

# This payload is broken!
broken_payload = '{"datacenter": "us-west-2", "hosts": ["web-01"'

import json

try:
    json.loads(broken_payload)
    print("Hello")
except json.JSONDecodeError:
    print("[ERROR]: Failed to parse payload. System configuration data is malformed.")

working_payload = '{"datacenter": "us-west-2", "hosts": ["web-01]"}'
try:
    working_parsed = json.loads(working_payload)
    print(working_parsed['non_existent_key'])
except KeyError:
    print("[ERROR]: Expected data attribute missing.")