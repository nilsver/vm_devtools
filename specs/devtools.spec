Name:           vm_devtools
Version:        1.0.0
Release:        1%{?dist}
Summary:        VMware ESXi dev tools

License:        Proprietary
BuildArch:      noarch
Requires:       python3, python3-pip, python3-dotenv, pyvmomi

%description
Tools for managing VMware VMs.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/usr/local/lib/vm_devtools
cp bin/* %{buildroot}/usr/local/bin/
cp lib/* %{buildroot}/usr/local/lib/vm_devtools/
cp setup_vm_devtools.sh %{buildroot}/usr/local/bin/setup_vm_devtools
chmod +x %{buildroot}/usr/local/bin/*
chmod +x %{buildroot}/usr/local/bin/setup_vm_devtools

%files
/usr/local/bin/vm_list_all
/usr/local/bin/vm_power_on
/usr/local/bin/vm_power_off
/usr/local/bin/vm_reboot
/usr/local/bin/vm_restore_snapshot
/usr/local/bin/setup_vm_devtools
/usr/local/lib/vm_devtools/*

%post
echo "Please run 'setup_vm_devtools' to configure your VMware credentials."

%changelog
* Mon Nov 17 2025 Nils Verschaeve <nverschaeve@redborder.com> - 1.0.0-1
- Initial package
