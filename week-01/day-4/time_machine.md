# ماشین زمان Git

در این تمرین با سه دستور برای بررسی تاریخچه و تغییرات پروژه آشنا شدم.

## 1. git log --oneline

برای نمایش تاریخچه کامیت‌ها به شکل خلاصه استفاده می‌شود.

**خروجی واقعی من:**

```text
5b448a8 Complete day 3 debug lab
4d0d7ee Complete week 1 day 3 weather card
5eb293e Merge branch 'main' of https://github.com/shawnmkarimi74-collab/intern-start
5e5eff0 Add day 2 log analysis exercise
bbea4d6 Create BUGLOG.md
ab01756 Create machine.md
75d67a7 Add echo_mini
d903c7a Add quiz
789a2a1 Fix README text
9451465 FIX README text
cdf4a15 Add README
bc8d905 Add hello.py
```

## 2. git show

برای مشاهده جزئیات یک کامیت، اطلاعات نویسنده، تاریخ و تغییرات فایل‌ها استفاده می‌شود.

**دستور اجراشده:**

```bash
git show 5b448a8
```

**نتیجه:** کامیت مربوط به تکمیل تمرین دیباگ روز سوم را بررسی کردم و دیدم فایل BUGLOG.md در آن ایجاد شده است.

## 3. git diff

برای مشاهده تفاوت تغییرات فایل‌ها استفاده می‌شود.

**دستور اجراشده:**

```bash
git diff
```

در ابتدا خروجی خالی بود، چون تغییر قابل نمایشی در فایل‌های تحت کنترل Git وجود نداشت.

بعد با دستور زیر فایل جدید README را برای بررسی تفاوت‌ها معرفی کردم:

```bash
git add -N week-01/day-4/README.md
```

پس از آن، دستور git diff خطوط جدید فایل را با علامت + نمایش داد.

## چیزی که یاد گرفتم

- git log تاریخچه کامیت‌ها را نشان می‌دهد.
- git show جزئیات یک کامیت را نمایش می‌دهد.
- git diff تفاوت تغییرات را نشان می‌دهد.
- فایل Untracked با فایل Modified تفاوت دارد.