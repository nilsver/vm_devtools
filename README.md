# VMware ESXi Dev Tools

This repository contains a set of command-line tools for managing VMware ESXi virtual machines.

## Installation

The tools are packaged as an RPM for easy installation.

### 1. Build the RPM

To build the RPM package, navigate to the root of this repository and run the `build.sh` script:

```bash
./build.sh
```

This will create an RPM file in `~/rpmbuild/RPMS/noarch/`.

### 2. Install Dependencies

Before installing the RPM, you need to install the `pyvmomi` library using `pip`:

```bash
pip install pyvmomi
```

### 3. Install the RPM

Once the RPM is built, you can install it using your system's package manager (e.g., `dnf` or `yum`):

```bash
sudo dnf install ./rpmbuild/RPMS/noarch/vm_devtools-1.0.0-1.noarch.rpm
# Or for older systems:
# sudo yum install ./rpmbuild/RPMS/noarch/vm_devtools-1.0.0-1.noarch.rpm
```

### 4. Configure the Tools

After installation, you need to configure your VMware ESXi credentials and main VM. Run the setup script:

```bash
sudo setup_vm_devtools
```

This script will prompt you for your VMware username, password, IP address, and the name of your main VM. This information will be saved in `/etc/vm_devtools/.env`.

## Usage

Once configured, you can use the following commands:

*   **`vm_list_all`**: Lists all virtual machines accessible by your configured VMware ESXi server.
*   **`vm_power_on [VM_NAME]`**: Powers on a specified virtual machine. If `VM_NAME` is not provided, it will power on the `VM_MAIN` configured during setup.
*   **`vm_power_off [VM_NAME]`**: Powers off a specified virtual machine. If `VM_NAME` is not provided, it will power off the `VM_MAIN` configured during setup.
*   **`vm_reboot [VM_NAME]`**: Reboots a specified virtual machine. If `VM_NAME` is not provided, it will reboot the `VM_MAIN` configured during setup.
*   **`vm_restore_snapshot [VM_NAME]`**: Restores the latest snapshot of a specified virtual machine. If `VM_NAME` is not provided, it will restore the latest snapshot of the `VM_MAIN` configured during setup.

**Example:**

```bash
vm_list_all
vm_power_on my_dev_vm
vm_restore_snapshot
```
