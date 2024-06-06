import tkinter as tk
from tkinter import PhotoImage, messagebox, simpledialog
import os

def create_ui(root, param_names):
    # 設置圖示路徑
    icons_path = "icons"
    icons = {}
    icon_files = {
        "read": "read.png",
        "save": "save.png",
        "add": "add.png",
        "delete": "delete.png",
        "copy": "copy.png",
        "check": "check.png",
        "trad": "trad.png",
        "simp": "simp.png"
    }

    for key, file in icon_files.items():
        path = os.path.join(icons_path, file)
        if os.path.exists(path):
            icons[key] = PhotoImage(file=path)
        else:
            icons[key] = None
            messagebox.showwarning("警告", f"找不到圖示文件：{path}")

    # 創建頂層框架來容納所有小部件
    top_frame = tk.Frame(root)
    top_frame.pack(fill=tk.BOTH, expand=True)

    # 創建並佈局讀取和保存檔案按鈕
    file_frame = tk.Frame(top_frame)
    file_frame.pack(side=tk.TOP, fill=tk.X, pady=5)

    read_button = tk.Button(file_frame, text="讀取技能檔案", compound=tk.LEFT, bg="#f0f0f0", fg="#000000")
    if icons["read"]:
        read_button.config(image=icons["read"])
    read_button.pack(side=tk.LEFT, padx=5)

    save_file_button = tk.Button(file_frame, text="保存技能檔案", compound=tk.LEFT, bg="#f0f0f0", fg="#000000")
    if icons["save"]:
        save_file_button.config(image=icons["save"])
    save_file_button.pack(side=tk.LEFT, padx=5)

    # 創建Listbox來顯示技能列表，並添加滾動條
    listbox_frame = tk.Frame(top_frame)
    listbox_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

    skill_listbox = tk.Listbox(listbox_frame, borderwidth=2, relief="groove")
    skill_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=skill_listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbar.config(width=20, relief='raised', bg="#d4d4d4")
    skill_listbox.config(yscrollcommand=scrollbar.set)

    # 創建操作List Box的按鈕框架
    listbox_button_frame = tk.Frame(top_frame)
    listbox_button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)

    add_button = tk.Button(listbox_button_frame, text="新增技能", compound=tk.LEFT, bg="#d4f1f9", fg="#000000")
    if icons["add"]:
        add_button.config(image=icons["add"])
    add_button.pack(fill=tk.X, pady=2)

    delete_button = tk.Button(listbox_button_frame, text="刪除技能", compound=tk.LEFT, bg="#fcd4d4", fg="#000000")
    if icons["delete"]:
        delete_button.config(image=icons["delete"])
    delete_button.pack(fill=tk.X, pady=2)

    copy_button = tk.Button(listbox_button_frame, text="複製技能", compound=tk.LEFT, bg="#f0f0f0", fg="#000000")
    if icons["copy"]:
        copy_button.config(image=icons["copy"])
    copy_button.pack(fill=tk.X, pady=2)

    check_button = tk.Button(listbox_button_frame, text="檢查重複ID", compound=tk.LEFT, bg="#f0f0f0", fg="#000000")
    if icons["check"]:
        check_button.config(image=icons["check"])
    check_button.pack(fill=tk.X, pady=2)

    convert_to_traditional_button = tk.Button(listbox_button_frame, text="轉繁體", compound=tk.LEFT, bg="#f0f0f0", fg="#000000")
    if icons["trad"]:
        convert_to_traditional_button.config(image=icons["trad"])
    convert_to_traditional_button.pack(fill=tk.X, pady=2)

    convert_to_simplified_button = tk.Button(listbox_button_frame, text="轉簡體", compound=tk.LEFT, bg="#f0f0f0", fg="#000000")
    if icons["simp"]:
        convert_to_simplified_button.config(image=icons["simp"])
    convert_to_simplified_button.pack(fill=tk.X, pady=2)

    # 創建一個框架來顯示54個欄目框
    param_frame = tk.Frame(top_frame)
    param_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)

    param_entries = []
    param_labels = []
    num_columns = 3
    num_rows = 18
    entry_font = ("Helvetica", 12)
    label_font = ("Helvetica", 12, "bold")

    for i in range(54):
        row = i % num_rows
        col = i // num_rows
        label = tk.Label(param_frame, text=param_names[i], font=label_font, background="#f0f0f0", padx=5, pady=5)
        label.grid(row=row, column=col*2, padx=5, pady=5, sticky=tk.E)
        entry = tk.Entry(param_frame, font=entry_font, borderwidth=2, relief="solid", background="#ffffff", foreground="#000000")
        entry.grid(row=row, column=col*2+1, padx=5, pady=5, sticky=tk.W)
        param_entries.append(entry)
        param_labels.append(label)

    # 創建保存按鈕
    save_button = tk.Button(param_frame, text="保存技能", compound=tk.LEFT, font=label_font, borderwidth=2, relief="raised", background="#4caf50", foreground="#ffffff")
    if icons["save"]:
        save_button.config(image=icons["save"])
    save_button.grid(row=num_rows, column=1, padx=5, pady=5, sticky=tk.W)

    # 創建編輯參數名稱按鈕
    edit_names_button = tk.Button(param_frame, text="編輯參數名稱", compound=tk.LEFT, font=label_font, borderwidth=2, relief="raised", background="#f0ad4e", foreground="#ffffff")
    edit_names_button.grid(row=num_rows, column=3, padx=5, pady=5, sticky=tk.W)

    return {
        "read_button": read_button,
        "save_file_button": save_file_button,
        "skill_listbox": skill_listbox,
        "add_button": add_button,
        "delete_button": delete_button,
        "copy_button": copy_button,
        "check_button": check_button,
        "convert_to_traditional_button": convert_to_traditional_button,
        "convert_to_simplified_button": convert_to_simplified_button,
        "save_button": save_button,
        "param_entries": param_entries,
        "param_labels": param_labels,
        "edit_names_button": edit_names_button
    }, icons
