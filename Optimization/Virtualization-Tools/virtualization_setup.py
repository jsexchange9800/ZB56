import subprocess

def setup_virtual_machine():
    """ راه‌اندازی ماشین مجازی """
    subprocess.run(["sudo", "virt-install", "--name", "my_vm", "--vcpus", "2", "--memory", "2048", "--disk", "size=10", "--os-type", "linux", "--cdrom", "/path/to/iso"])

if __name__ == "__main__":
    setup_virtual_machine()
