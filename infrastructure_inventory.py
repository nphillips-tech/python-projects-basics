#!/usr/bin/env python3

#Goal: The goal is to learn how to store, access, and manipulate groups of data using Python Lists (ordered sequences) and Dictionaries (Key-Value mappings) to represent real-world infrastructure objects.
#Objective:
#Write a script that does the following:
#Create a List called monitoring_targets containing at least three IP address strings (e.g., "192.168.1.10", "192.168.1.11").
#Append a fresh IP address ("192.168.1.50") to that list using code (don't hardcode it into the initial list declaration).
#Create a Dictionary called production_server that acts as an asset asset profile. It must contain the following keys and relevant values:
#    hostname (string)
#    environment (string)
#    cpu_cores (integer)
#    ram_gb (integer)
#    active (boolean - True or False)
#Print out a clean, single-sentence status report to the terminal by pulling values directly out of your dictionary using an f-string.

"Server prod-app-01 is active with 4 CPU cores and 16GB of RAM."
monitoring_targets = ["10.0.0.1","10.123.45.102","192.168.48.33"]
monitoring_targets.append("192.168.1.50")

production_server = {
    "hostname":"prod-1",
    "environment":"production",
    "cpu_cores":8,
    "ram_gb":32,
    "active":True
}

#print(production_server.get("hostname"))
print(f"Server {production_server.get('hostname')} is active with {production_server.get('cpu_cores')} CPU cores and {production_server.get('ram_gb')} of RAM.")