from datetime import datetime

def clock():
    return datetime.now().strftime("%H:%M")

def calc(a, b):
    return a + b

rules = {
    "hello": "سلام! من Echo-mini هستم 👋",
    "price": "پلن حرفه‌ای ماهی 10 دلار است.",
    "help": "بنویس: hello، price، time، add یا bye",
    "python": "هر روز یک خط  کد بنویس"
}

print("🤖 Echo-mini روشن شد. برای خروج بنویس bye")
while True:
    msg = input("تو: ").strip().lower()
    if msg == "bye":
        print("Echo-mini: خداحافظ! 👋")
        break
    elif msg in rules:
        print("Echo-mini:", rules[msg])
    elif msg == "time":
        print("Echo-mini: ساعت", clock(), "است ⏰")
    elif msg == "add":
        a = int(input("عدد اول: "))
        b = int(input("عدد دوم: "))
        print("Echo-mini: جواب", calc(a, b))
    else:
        print("Echo-mini: متوجه نشدم 🤔 بنویس help")

