#!/usr/bin/env python3
import os
from vm_common import connect_vmware, get_vm_by_name
from pyVmomi import vim

si, content = connect_vmware()
container = content.viewManager.CreateContainerView(
    content.rootFolder, [vim.VirtualMachine], True
)

vms = container.view

rows = []
for vm in vms:
    name = vm.name
    power = vm.runtime.powerState if vm.runtime else "Unknown"

    if power == "poweredOn":
        colored = "\033[92mOn\033[0m"
        raw = "On"
    elif power == "poweredOff":
        colored = "\033[91mOff\033[0m"
        raw = "Off"
    else:
        colored = "\033[93mSuspended\033[0m"
        raw = "Suspended"

    rows.append((raw, colored, name))

max_len = max(len(r[0]) for r in rows)
print(f"Found {len(vms)} VMs:")
for raw, colored, name in rows:
    print(f"{colored.ljust(max_len + 3)} {name}")
