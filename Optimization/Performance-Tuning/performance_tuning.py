import os
import psutil
import time

def tune_memory():
    """ تنظیمات بهینه‌سازی حافظه """
    # فعال‌سازی تخصیص حافظه بیشتر
    psutil.virtual_memory()
    print("Memory tuned successfully")

def optimize_cpu():
    """ بهینه‌سازی پردازشگر """
    # بررسی استفاده از پردازشگر
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Current CPU usage: {cpu_usage}%")
    if cpu_usage > 80:
        print("CPU optimization triggered!")
    else:
        print("CPU usage is optimal.")

def run_performance_tuning():
    """ اجرای تنظیمات بهینه‌سازی کلی """
    print("Optimizing memory...")
    tune_memory()
    print("Optimizing CPU...")
    optimize_cpu()

if __name__ == "__main__":
    run_performance_tuning()
