#!/bin/bash

# نصب KVM
sudo apt update
sudo apt install -y qemu-kvm libvirt-bin bridge-utils virt-manager

# بررسی وضعیت نصب
sudo systemctl status libvirtd
echo "Hypervisor setup completed successfully!"
