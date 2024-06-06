import tkinter as tk
from tkinter import filedialog, messagebox
import json

def save_param_names(param_names, filename="param_names.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(param_names, file, ensure_ascii=False, indent=4)

def load_param_names(filename="param_names.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return [f"參數{i+1}" for i in range(54)]

def read_skill_file(skill_listbox, skills_data):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.readlines()

        # 清空現有的Listbox和技能數據
        skill_listbox.delete(0, tk.END)
        skills_data.clear()

        for line in data:
            values = line.strip().split('\t')
            skills_data.append(values)
            skill_listbox.insert(tk.END, values[1])  # 使用技能名稱作為列表項

    except Exception as e:
        messagebox.showerror("Error", f"Failed to read file: {str(e)}")

def save_skill_file(skills_data):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for skill in skills_data:
                file.write('\t'.join(skill) + '\n')
        messagebox.showinfo("成功", "技能檔案已保存")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {str(e)}")
