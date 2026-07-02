#!/usr/bin/env python3

import json

eligible_servers = []
malformed_records_count = 0

with open ("raw_inventory.txt", "r") as raw_inventory:
    for line in raw_inventory:
        try:
            server_data = json.loads(line)
        except json.JSONDecodeError as e:
            print(f"[WARNING]: There has been an error with parsing the data -> {e}.")
            malformed_records_count = malformed_records_count + 1
        else:
            if "ram" not in server_data:
                print("[WARN] stage-app-01 skipped: Missing RAM specification.")
                continue
            if "ram" in server_data and "cpu" in server_data and server_data["cpu"] >= 2 and server_data["ram"] >= 8:
                eligible_servers.append(server_data)
                

with open("migration_report.txt", "w") as report:
    # Add \n at the end of your strings to push the next write down a line
    report.write("==============================\n")
    report.write("AWS MIGRATION READINESS REPORT\n")
    report.write("==============================\n")
    report.write(f"Total Eligible Servers: {len(eligible_servers)}\n")
    report.write(f"Total Malformed Records Skipped: {malformed_records_count}\n\n")
   
    report.write("The following servers are cleared for AWS migration:\n")
    
    # Instead of printing the length here, loop through your passing servers!
    for server in eligible_servers:
        report.write(f"- {server['hostname']} ({server['environment']})\n")
