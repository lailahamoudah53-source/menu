import tkinter as tk
from tkinter import messagebox
import sqlite3
import socket
from datetime import datetime

# إعداد قاعدة بيانات محلية
conn = sqlite3.connect("restaurant.db")
c = conn.cursor()
c.execute(("""CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_number INTEGER,
            item TEXT,
            price REAL,
            quantity INTEGER,
            total REAL,
            payment_method TEXT,
            datetime TEXT)"""))
conn.commit()

# قائمة الطعام (يمكن تعديلها حسب كل مطعم)
menu = {
    "شاورما": 5.0,
    "بيتزا": 8.0,
    "مشروب": 2.0,
    "سلطة": 3.0
}

# إدخال رقم الطاولة
table_number = int(input("ادخل رقم الطاولة: "))

# إعداد اتصال بالشبكة المحلية (مطبخ)
SERVER_HOST = '127.0.0.1'  # عنوان جهاز المطبخ على الشبكة المحلية
SERVER_PORT = 5000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((SERVER_HOST, SERVER_PORT))
except:
    print("لم يتم الاتصال بشاشة المطبخ. سيتم حفظ الطلب محليًا فقط.")

# واجهة المستخدم
root = tk.Tk()
root.title(f"طاولة رقم {table_number}")

tk.Label(root, text="اختر الطبق:").grid(row=0, column=0)
item_var = tk.StringVar(value=list(menu.keys())[0])
tk.OptionMenu(root, item_var, *menu.keys()).grid(row=0, column=1)

tk.Label(root, text="الكمية:").grid(row=1, column=0)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=1, column=1)

tk.Label(root, text="طريقة الدفع:").grid(row=2, column=0)
payment_var = tk.StringVar(value="كاش")
tk.OptionMenu(root, payment_var, "كاش", "محفظة").grid(row=2, column=1)

def submit_order():
    item = item_var.get()
    qty = quantity_entry.get()
    payment = payment_var.get()
   
    if not qty.isdigit() or int(qty) <= 0:
        messagebox.showwarning("خطأ", "ادخل كمية صحيحة")
        return
   
    qty = int(qty)
    price = menu[item]
    total = price * qty
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
    # حفظ محلي
    c.execute("""INSERT INTO orders (table_number, item, price, quantity, total, payment_method, datetime)
                 VALUES (?, ?, ?, ?, ?, ?, ?)""",
              (table_number, item, qty,price,total, payment, now))
    conn.commit()
   
    # إرسال للمطبخ
    try:
        client_socket.send(f"{table_number}|{item}|{qty}|{payment}|{now}".encode())
    except:
        print("لم يتم إرسال الطلب لشاشة المطبخ.")
   
    messagebox.showinfo("تم الطلب", f"تم إرسال الطلب: {item} x{qty}\nالمجموع: ${total:.2f}")
    quantity_entry.delete(0, tk.END)

tk.Button(root, text="إرسال الطلب", command=submit_order).grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()
client_socket.close()

#;;;;;;كود المطبخ او شاشة المطبخ

import socket
import threading

orders = []

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            orders.append(data)
            update_screen()
        except:
            break
    client_socket.close()

def update_screen():
    print("\n--- طلبات المطبخ ---")
    for o in orders:
        print(o)
    print("-------------------\n")

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)
print("شاشة المطبخ جاهزة...")

while True:
    client_sock, addr = server_socket.accept()
    print(f"اتصال من: {addr}")
    threading.Thread(target=handle_client, args=(client_sock,)).start()
