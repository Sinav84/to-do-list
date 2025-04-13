import tkinter as tk
from tkinter import messagebox

def add_task():
    title = title_entry.get()
    details = details_entry.get()
    person = person_entry.get()
    deadline = deadline_entry.get()

    if title and person and deadline:
        task_str = f"عنوان: {title} | مسئول: {person} | ددلاین: {deadline}\nجزئیات: {details}"
        listbox.insert(tk.END, task_str)
        # پاک کردن فیلدها
        title_entry.delete(0, tk.END)
        details_entry.delete(0, tk.END)
        person_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("خطا", "لطفاً عنوان، مسئول و ددلاین را وارد کنید.")

def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("هشدار", "لطفاً یک آیتم برای حذف انتخاب کنید.")

# رابط گرافیکی
root = tk.Tk()
root.title("مدیریت وظایف با جزئیات")
root.geometry("600x600")

# ورودی‌ها
tk.Label(root, text="عنوان وظیفه:").pack()
title_entry = tk.Entry(root, width=60)
title_entry.pack(pady=5)

tk.Label(root, text="جزئیات:").pack()
details_entry = tk.Entry(root, width=60)
details_entry.pack(pady=5)

tk.Label(root, text="نام مسئول:").pack()
person_entry = tk.Entry(root, width=60)
person_entry.pack(pady=5)

tk.Label(root, text="ددلاین (مثلاً 1403/02/20 - 14:00):").pack()
deadline_entry = tk.Entry(root, width=60)
deadline_entry.pack(pady=5)

tk.Button(root, text="➕ اضافه کردن وظیفه", command=add_task).pack(pady=10)

listbox = tk.Listbox(root, width=90, height=15)
listbox.pack(pady=10)

tk.Button(root, text="❌ حذف وظیفه انتخاب‌شده", command=delete_task).pack(pady=5)

root.mainloop()
