import numpy as np
from scipy.integrate import quad

# **ماژول معادله حمزه (ماژول اصلی)**
def hamzah_equation(x):
    return np.exp(-x) * np.sin(x)

def compute_hamzah_integral():
    integral_result, error = quad(hamzah_equation, 0, 10)
    return integral_result, error

# **هسته اصلی سیستم**
class Core:
    def __init__(self):
        self.modules = {}  # ذخیره ماژول‌ها

    def register_module(self, name, module):
        self.modules[name] = module

    def handle_request(self, question):
        # اول بررسی می‌کنیم آیا ماژولی برای این سوال وجود دارد یا نه
        for module_name, module in self.modules.items():
            if module_name in question:
                return module.answer(question)
        
        # اگر ماژولی پیدا نشد، از ماژول تحلیل معادله حمزه استفاده می‌کنیم
        if "حمزه" in question:
            return self.modules["تحلیل حمزه"].answer(question)
        
        # اگر هیچ کدام نبود، پاسخ پیش‌فرض
        return "متأسفم، نمی‌توانم به این سوال پاسخ دهم."

# **ماژول پاسخ‌های استاندارد**
class StandardResponseModule:
    def answer(self, question):
        responses = {
            "چگونه حال شما": "من یک برنامه هوش مصنوعی هستم و احساس ندارم، اما می‌توانم در تحلیل داده‌ها به شما کمک کنم!",
            "آب و هوا امروز چطور است": "آب و هوا بسته به موقعیت جغرافیایی شما تغییر می‌کند. برای اطلاعات دقیق‌تر می‌توانید از سرویس‌های هواشناسی استفاده کنید.",
        }
        for key in responses:
            if key in question:
                return responses[key]
        return "سوال شما جالب است! من می‌توانم از طریق تحلیل معادله حمزه به آن پاسخ دهم."

# **ماژول تحلیل معادله حمزه**
class HamzahAnalysisModule:
    def answer(self, question):
        integral_result, error = compute_hamzah_integral()
        explanation = f"""
        🔹 **تحلیل علمی بر اساس معادله حمزه**
        ✅ **مقدار محاسبه‌شده بر اساس معادله حمزه:**
           **{integral_result} (±{error})**  
        """
        return explanation

# **ماژول فیزیک**
class PhysicsModule:
    def answer(self, question):
        if "سرعت نور" in question:
            return "سرعت نور در خلأ حدود ۱,۰۸۰,۰۰۰,۰۰۰ کیلومتر بر ساعت است."
        elif "انرژی جنبشی" in question:
            return "انرژی جنبشی با فرمول ۰٫۵ × جرم × سرعت² محاسبه می‌شود."
        else:
            return "سوال شما در حوزه فیزیک است، اما نیاز به اطلاعات بیشتری دارم."

# **ماژول ریاضی**
class MathModule:
    def answer(self, question):
        if "انتگرال" in question:
            return "انتگرال‌گیری یکی از ابزارهای کلیدی در ریاضیات است که برای محاسبه مساحت زیر منحنی، حجم، و مدل‌سازی سیستم‌های فیزیکی استفاده می‌شود."
        elif "مشتق" in question:
            return "مشتق‌گیری برای محاسبه نرخ تغییرات یک تابع استفاده می‌شود."
        else:
            return "سوال شما در حوزه ریاضی است، اما نیاز به اطلاعات بیشتری دارم."

# **اجرای تست**
if __name__ == "__main__":
    # ایجاد هسته سیستم
    core = Core()
    
    # ثبت ماژول‌ها
    core.register_module("پاسخ استاندارد", StandardResponseModule())
    core.register_module("تحلیل حمزه", HamzahAnalysisModule())
    core.register_module("فیزیک", PhysicsModule())
    core.register_module("ریاضی", MathModule())

    # سوالات نمونه
    questions = [
        "چگونه حال شما؟",
        "آب و هوا امروز چطور است؟",
        "سرعت نور چقدر است؟",
        "انرژی جنبشی چیست؟",
        "تحلیل معادله حمزه برای این سوال چیست؟"
    ]

    # پاسخ به سوالات
    for q in questions:
        print(f"❓ **سوال:** {q}")
        print(f"📚 **پاسخ:** {core.handle_request(q)}")
        print("———————————————————————")
