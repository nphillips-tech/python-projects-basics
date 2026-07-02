#!/usr/bin/env python3

#The Goal: The goal is to learn how to nest dictionaries inside a list and use loops to look inside each asset profile dynamically.
#Objective
#Create a single list called server_fleet.
#Inside that list, drop three separate dictionaries. Each dictionary represents a server and should have keys for hostname, environment, and os_version (an integer like 20 or 22 representing Ubuntu versions).
#    Make one server named "prod-app-01" in environment "production" with os_version: 20.
#    Make the second named "stage-web-01" in environment "staging" with os_version: 22.
#    Make the third named "dev-db-01" in environment "development" with os_version: 20.
#Write a for loop that iterates through your server_fleet.
#Inside the loop, evaluate each server's OS version. If the os_version is less than 22, print a compliance warning to the terminal (e.g., [OUT OF COMPLIANCE] prod-app-01 is running an outdated OS!).


##Notes
#First, I created the three dictionaries. Each one with it's own naming convention, followed by the necessary curly brackets and the key:value pairs. Each string has quotes (all of the names) and integers are simply input (like the OS versions)..
production_dict = {
    "hostname":"prod-app-01",
    "environment":"production",
    "os_version":20
}

staging_dict = {
    "hostname":"stage-web-01",
    "environment":"staging",
    "os_version":22
}

development_dict = {
    "hostname":"dev-db-01",
    "environment":"development",
    "os_version":20
}

#Next I created the list containing each dictionary. One thing I messed up orignally was thinking that I needed to put the dictionary names within quotes and then call them out as variables with curly brackets since quotes indicate strings, however since they are already predefined variables, I simply needed to just define them without quotes or curly brackets within the listing format of square brackets and comma separation.
server_fleet = [production_dict,staging_dict,development_dict]

#Finally, the for loop calls in "for each 'server' variable in the 'server fleet', we want to create a variable named 'os_version' that gets the value of the the aptly named key and then evaluate that if within the dictionary we evaluate an os_version and it happens to be less than 22, print the out of compliance message leveraging the respective server's name"
for server in server_fleet:
    os_version = server.get("os_version")

    if os_version and os_version < 22:
        print(f"[OUT OF COMPLIANCE] {server.get('hostname')} is running an outdates OS!")