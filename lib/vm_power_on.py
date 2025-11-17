#!/usr/bin/env python3
import os, sys
from vm_common import connect_vmware, get_vm_by_name, power_on

vm_name = sys.argv[1] if len(sys.argv) > 1 else os.getenv("VM_MAIN")
si, content = connect_vmware()
vm = get_vm_by_name(content, vm_name)

if not vm:
    print(f"VM '{vm_name}' not found.")
    sys.exit(1)

result = power_on(vm)
print(f"Power ON: {result}")
