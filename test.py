#!/usr/bin/env python3
with open("/home/nick/system.log", "r") as testfilevar:
    for line in testfilevar:
        if "INFO" in line:
            continue
        else:
            print("[ALERT FOUND] " + line )
