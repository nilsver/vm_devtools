import os
import atexit
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

def connect_vmware():
    host = os.getenv("VM_IP")
    user = os.getenv("VM_USERNAME")
    pwd  = os.getenv("VM_PASSWORD")

    si = SmartConnect(
            host=host,
            user=user,
            pwd=pwd,
            disableSslCertValidation=True
    )
    atexit.register(Disconnect, si)
    return si, si.RetrieveContent()

def get_vm_by_name(content, name):
    container = content.viewManager.CreateContainerView(
            content.rootFolder, [vim.VirtualMachine], True
    )
    for vm in container.view:
        if vm.name == name:
            return vm
    return None

def power_on(vm):
    if vm.runtime.powerState == "poweredOn":
        return "already_on"
    task = vm.PowerOn()
    return "started"

def power_off(vm):
    if vm.runtime.powerState == "poweredOff":
        return "already_off"
    task = vm.PowerOff()
    return "stopping"

def reboot_vm(vm):
    try:
        vm.RebootGuest()
        return "guest_reboot"
    except:
        vm.ResetVM_Task()
        return "hard_reset"

def restore_latest_snapshot(vm):
    if not vm.snapshot or not vm.snapshot.rootSnapshotList:
        return "no_snapshot"

    # find most recent snapshot
    def flatten(snaps):
        arr = []
        for s in snaps:
            arr.append(s)
            arr.extend(flatten(s.childSnapshotList))
        return arr

    snaps = flatten(vm.snapshot.rootSnapshotList)
    latest = max(snaps, key=lambda s: s.createTime)

    task = latest.snapshot.RevertToSnapshot_Task()
    return f"restoring {latest.name}"


