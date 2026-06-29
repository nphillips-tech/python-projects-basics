#!/usr/bin/env python3
## Goal = The goal for this hour is to learn how to evaluate system states using comparison operators and implement conditional if/elif/else blocks to prevent math errors or bad inputs from crashing your script.

deployment_environment = input("Please identify the Deployment Environment: ").lower()
storage_capacity_percentage = input("Please provide the current storage capacity use percentage: ")

storage_capacity_digit = int(storage_capacity_percentage)

if not storage_capacity_percentage.isdigit():
    print("Error - please submit a response with digits only.")
else:
    storage_capacity_digit = int(storage_capacity_percentage)

    if storage_capacity_digit > 100 or storage_capacity_digit < 0:
        print("Error - please submit a valid number between 0 and 100.")
    elif deployment_environment == "production" and storage_capacity_digit > 80:
        print("[CRITICAL] Storage threshold exceeded for Production! Deployment Halted.")
    elif deployment_environment == "staging" and storage_capacity_digit > 90:
        print("[WARNING] Staging resource warning.")
    else:
        print("[SUCCESS] Environment pre-check passed. Proceeding with deployment.")