import subprocess

def list_vms():
    """ لیست ماشین‌های مجازی """
    result = subprocess.run(["virsh", "list", "--all"], capture_output=True, text=True)
    print(result.stdout)

def start_vm(vm_name):
    """ شروع ماشین مجازی """
    subprocess.run(["virsh", "start", vm_name])

def stop_vm(vm_name):
    """ توقف ماشین مجازی """
    subprocess.run(["virsh", "shutdown", vm_name])

if __name__ == "__main__":
    list_vms()
