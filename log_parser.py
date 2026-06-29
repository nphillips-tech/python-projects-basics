#!/usr/bin/env python3
#!/usr/bin/env python3
with open("/home/nick/system.log", "r") as test_file:
    for line in test_file:
        if "INFO" in line:
            continue
        else:
            print(f"[ALERT FOUND] {line.rstrip()}")
