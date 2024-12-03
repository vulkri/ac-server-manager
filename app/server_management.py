import subprocess
import time
import uuid

# Save processes to db to start them when app is restarted?
servers = []

# Start server process
def start_server(preset, id, log_file):
    cwd = "../assettoServer"
    command = f"../assettoServer/AssettoServer -p {preset}"
    log_file = f"logs/{log_file}"

    with open(log_file, 'w') as log:
        process = subprocess.Popen(
            command, cwd=cwd, stdout=log, stderr=log, shell=True
        )
    servers.append({"id": id, "process": process, "log_file": log_file, "command": command})

# Monitor server process
def monitor_servers():
    for server in servers:
        process = server['process']
        if process.poll() is None:
            print(f"Server {server['id']} {server['command']} is still running.")
        else:
            print(f"Process {server['id']} {server['command']} has terminated.")

# Run monitor in the background
def background_monitor():
    while True:
        monitor_servers()
        time.sleep(5)  

