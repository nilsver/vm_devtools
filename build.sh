#!/bin/bash
set -e

# Ensure rpmbuild exists
if ! command -v rpmbuild &> /dev/null; then
    echo "Error: rpmbuild is not installed."
    exit 1
fi

# Prepare build directories
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

# Copy spec and sources
cp specs/devtools.spec ~/rpmbuild/SPECS/
cp -r bin lib setup_vm_devtools.sh ~/rpmbuild/SOURCES/

# Build RPM
rpmbuild -bb ~/rpmbuild/SPECS/devtools.spec

if [ $? -eq 0 ]; then
    echo "RPM built successfully. Find it in ~/rpmbuild/RPMS/noarch/"
else
    echo "RPM build failed."
    exit 1
fi
