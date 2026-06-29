#!/usr/bin/env python3
## Goal = Create a script that acts as a basic System Resource Calculator.
name_of_server = input("What is the name of the server?: ")
total_ram_gigs = input("What is the total amount of allocated RAM for this server?: ")
application_container_ram_gigs = input("What is the total amount of RAM consumed by a single application container?: ")

total_container_capacity = (int(total_ram_gigs)//float(application_container_ram_gigs))
clean_capacity_count = int(total_container_capacity)
remainder_container_capacity = (int(total_ram_gigs)%float(application_container_ram_gigs))

print(f"The {name_of_server} has a total of {total_ram_gigs}. Each application container uses {application_container_ram_gigs}GB. Therefore, {name_of_server} can support {clean_capacity_count} containers. Leftover RAM that cannot support another full container comes out to a total of {remainder_container_capacity:.2f}GB(s)")