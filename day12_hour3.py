#!/usr/bin/env python3
## Goal = The goal for this hour is to learn how to evaluate system states using comparison operators and implement conditional if/elif/else blocks to prevent math errors or bad inputs from crashing your script.
# === LOOP 1: Validate Environment Name ===
while True:
    deployment_environment = input("Please identify the Deployment Environment: ").lower()
    if deployment_environment in ["development", "staging", "production"]:
        break  # Success! Break the loop and move to the next section
    
    print("Error - please type a correct deployment environment name (development/staging/production).")


# === LOOP 2: Validate Storage Capacity ===
while True:
    storage_capacity_percentage = input("Please provide the current storage capacity use percentage: ")
    
    # Check 1: Is it even a number?
    if not storage_capacity_percentage.isdigit():
        print("Error - please submit a response with digits only.")
        continue  # Skip the rest of the loop and prompt again
    
    # Check 2: It's a number, so cast it and check boundaries
    storage_capacity_digit = int(storage_capacity_percentage)
    if storage_capacity_digit > 100 or storage_capacity_digit < 0:
        print("Error - please submit a valid number between 0 and 100.")
    else:
        break  # Success! Out of the loop we go


# === FINAL EVALUATION ===
if deployment_environment == "production" and storage_capacity_digit > 80:
    print("[CRITICAL] Storage threshold exceeded for Production! Deployment Halted.")
elif deployment_environment == "staging" and storage_capacity_digit > 90:
        print("[WARNING] Staging resource warning.")
else:
    print("[SUCCESS] Environment pre-check passed. Proceeding with deployment.")