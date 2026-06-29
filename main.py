# روش ۱: ساده‌ترین حالت
with open("tasks.txt", "r", encoding="utf-8") as f:
    content = f.read()          # همه‌ی فایل به‌صورت یک رشته
    
# روش ۲: خواندن خط به خط
with open("tasks.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()       # لیست خطوط (با \n در انتها)

# روش ۳: تمیزترین حالت
with open("tasks.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]
    # هم \n را حذف می‌کند، هم خطوط خالی را رد می‌کند

# "w" → اگر فایل وجود داشته باشد، محتوایش پاک می‌شود
with open("tasks.txt", "w", encoding="utf-8") as f:
    f.write("خرید نان\n")
    f.write("مطالعه پایتون\n")

# "a" → append: اضافه کردن به انتهای فایل (محتوای قبلی حفظ می‌شود)
with open("tasks.txt", "a", encoding="utf-8") as f:
    f.write("ورزش صبحگاهی\n")

# نوشتن یک لیست
tasks = ["خرید نان", "مطالعه", "ورزش"]
with open("tasks.txt", "w", encoding="utf-8") as f:
    f.writelines(task + "\n" for task in tasks)