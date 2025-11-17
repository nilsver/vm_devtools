#!/bin/bash
set -e

# Ensure rpmbuild exists
if ! command -v rpmbuild &> /dev/null; then
    echo "Error: rpmbuild is not installed."
    exit 1
fi

# Prepare build directories
mkdir -p ./rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

# Create a source tarball
SRCDIR=vm_devtools-1.0.0
CURRENT_DIR=$(pwd)
rm -rf /tmp/$SRCDIR
mkdir -p /tmp/$SRCDIR
cp -r bin lib setup_vm_devtools.sh /tmp/$SRCDIR/
(cd /tmp && tar --exclude='*/__pycache__' -czf "$CURRENT_DIR/rpmbuild/SOURCES/$SRCDIR.tar.gz" $SRCDIR)

# Copy spec
cp specs/devtools.spec ./rpmbuild/SPECS/

# Build RPM
rpmbuild -bb --define "_topdir $(pwd)/rpmbuild" ./rpmbuild/SPECS/devtools.spec

if [ $? -eq 0 ]; then
    echo "RPM built successfully. Find it in ./rpmbuild/RPMS/noarch/"
else
    echo "RPM build failed."
    exit 1
fi
