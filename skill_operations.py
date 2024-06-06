import tkinter as tk
from tkinter import messagebox
from collections import Counter
from opencc import OpenCC


def add_skill(skill_listbox, skills_data, param_entries):
    new_skill = [entry.get() for entry in param_entries]
    skills_data.append(new_skill)
    skill_listbox.insert(tk.END, "新技能")
    skill_listbox.select_clear(0, tk.END)
    skill_listbox.selection_set(tk.END)


def delete_skill(skill_listbox, skills_data, param_entries):
    selected_index = skill_listbox.curselection()
    if not selected_index:
        return

    skill_index = selected_index[0]
    del skills_data[skill_index]
    skill_listbox.delete(skill_index)
    clear_entries(param_entries)


def copy_skill(skill_listbox, skills_data, current_skill_index):
    if current_skill_index is None:
        return

    copied_skill = skills_data[current_skill_index][:]
    skills_data.append(copied_skill)
    skill_listbox.insert(tk.END, copied_skill[1])
    skill_listbox.select_clear(0, tk.END)
    skill_listbox.selection_set(tk.END)


def clear_entries(param_entries):
    for entry in param_entries:
        entry.delete(0, tk.END)


def check_duplicate_ids(skills_data):
    id_counter = Counter(skill[0] for skill in skills_data)
    duplicates = {skill_id: count for skill_id, count in id_counter.items() if count > 1}

    if not duplicates:
        messagebox.showinfo("檢查結果", "無重複ID")
    else:
        duplicate_list = "\n".join([f"ID {skill_id} 重複 {count} 次" for skill_id, count in duplicates.items()])
        messagebox.showwarning("檢查結果", f"發現重複ID:\n\n{duplicate_list}\n\n總共有 {len(duplicates)} 個重複ID")


def suggest_new_id(skills_data):
    ids = [int(skill[0]) for skill in skills_data if skill[0].isdigit()]
    max_id = max(ids) if ids else 0
    return str(max_id + 1)


def save_skill(skills_data, param_entries, current_skill_index):
    if current_skill_index is None:
        messagebox.showwarning("Warning", "請選擇一個技能進行保存")
        return

    skill_index = current_skill_index
    skill_id = param_entries[0].get()

    # 檢查是否有重複的ID
    if any(skill[0] == skill_id for i, skill in enumerate(skills_data) if i != skill_index):
        suggested_id = suggest_new_id(skills_data)
        messagebox.showwarning("Warning", f"ID 已重複，請使用一個新的ID。建議ID：{suggested_id}")
        return

    for i in range(54):
        skills_data[skill_index][i] = param_entries[i].get()

    # 保持選中狀態
    return True


def convert_names(skills_data, conversion_type):
    if conversion_type == "s2t":
        converter = OpenCC('s2t')
    elif conversion_type == "t2s":
        converter = OpenCC('t2s')
    else:
        return

    for skill in skills_data:
        skill[1] = converter.convert(skill[1])
