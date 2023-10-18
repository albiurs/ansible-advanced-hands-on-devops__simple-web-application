#! /usr/bin/python

import json
import argparse

# Get inventory data from source - CMDB or any other API
def get_inventory_data():
    return {
        "databases": {
            "hosts": ["db_server"],
            "vars": {
                "ansible_ssh_pass": "passw0rd",
                "ansible_ssh_host": "192.168.1.1"
            }
        },
        "web": {
            "hosts": ["web_server"],
            "vars": {
                "ansible_ssh_pass": "passw0rd",
                "ansible_ssh_host": "192.168.1.2"
            }
        }
    }

def read_cli_args():
    global args
    parser = argparse.ArgumentParser()
    # ./inventory.py --list
    parser.add_argument('--list', action='store_true')
    # ./inventory.py --host xyz
    parser.add_argument('--host', action='store')
    args = parser.parse_args()

# Default main function
if __name__ == "__main__":
    global args
    read_cli_args()
    invventory_data = get_inventory_data()
    if args and args.list:
        print(json.dumps(invventory_data))
    elif args and args.host:
        print(json.dumps({'_meta': {'hostsvars': {}}}))
