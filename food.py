import tkinter as tk
from tkinter import messagebox
import sqlite3

# إنشاء قاعدة بيانات محلية
conn = sqlite3.connect("restaurant.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_number TEXT,
            item TEXT,
            quantity INTEGER)""")
conn.commit()

# واجهة المستخدم
def submit_order():
    table = table_entry.get()
    item = item_entry.get()
    qty = quantity_entry.get()
    if table and item and qty:
        c.execute("INSERT INTO orders (table_number, item, quantity) VALUES (?, ?, ?)",
                  (table, item, int(qty)))
        conn.commit()
        messagebox.showinfo("تم الطلب", f"تم إرسال الطلب: {item} x{qty} للطاولة {table}")
        table_entry.delete(0, tk.END)
        item_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("خطأ", "املأ جميع الحقول")

root = tk.Tk()
root.title("نظام الطلبات الداخلي")

tk.Label(root, text="رقم الطاولة:").grid(row=0, column=0)
table_entry = tk.Entry(root)
table_entry.grid(row=0, column=1)

tk.Label(root, text="الوجبة:").grid(row=1, column=0)
item_entry = tk.Entry(root)
item_entry.grid(row=1, column=1)

tk.Label(root, text="الكمية:").grid(row=2, column=0)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=2, column=1)

tk.Button(root, text="إرسال الطلب", command=submit_order).grid(row=3, column=0, columnspan=2)

root.mainloop()
