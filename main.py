import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from file_operations import read_skill_file, save_skill_file, load_param_names, save_param_names
from skill_operations import add_skill, delete_skill, copy_skill, clear_entries, check_duplicate_ids, save_skill, convert_names
from ui_components import create_ui

class SkillEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("技能編輯器")

        self.param_names = load_param_names()
        self.ui, self.icons = create_ui(root, self.param_names)

        # 綁定按鈕事件
        self.ui["read_button"].config(command=self.read_file)
        self.ui["save_file_button"].config(command=self.save_file)
        self.ui["add_button"].config(command=self.add_skill)
        self.ui["delete_button"].config(command=self.delete_skill)
        self.ui["copy_button"].config(command=self.copy_skill)
        self.ui["check_button"].config(command=self.check_duplicates)
        self.ui["convert_to_traditional_button"].config(command=self.convert_to_traditional)
        self.ui["convert_to_simplified_button"].config(command=self.convert_to_simplified)
        self.ui["save_button"].config(command=self.save_skill)
        self.ui["edit_names_button"].config(command=self.edit_param_names)

        self.ui["skill_listbox"].bind('<<ListboxSelect>>', self.on_skill_select)

        # 保存當前技能數據
        self.skills_data = []
        self.current_skill_index = None

    def read_file(self):
        read_skill_file(self.ui["skill_listbox"], self.skills_data)

    def save_file(self):
        save_skill_file(self.skills_data)

    def add_skill(self):
        add_skill(self.ui["skill_listbox"], self.skills_data, self.ui["param_entries"])
        self.select_last_skill()

    def delete_skill(self):
        delete_skill(self.ui["skill_listbox"], self.skills_data, self.ui["param_entries"])
        self.current_skill_index = None

    def copy_skill(self):
        copy_skill(self.ui["skill_listbox"], self.skills_data, self.current_skill_index)
        self.select_last_skill()

    def save_skill(self):
        if save_skill(self.skills_data, self.ui["param_entries"], self.current_skill_index):
            skill_index = self.current_skill_index
            # 保持選中狀態
            self.ui["skill_listbox"].selection_set(skill_index)

    def check_duplicates(self):
        check_duplicate_ids(self.skills_data)

    def convert_to_traditional(self):
        convert_names(self.skills_data, "s2t")
        self.update_listbox()

    def convert_to_simplified(self):
        convert_names(self.skills_data, "t2s")
        self.update_listbox()

    def update_listbox(self):
        self.ui["skill_listbox"].delete(0, tk.END)
        for skill in self.skills_data:
            self.ui["skill_listbox"].insert(tk.END, skill[1])

    def on_skill_select(self, event):
        selected_index = self.ui["skill_listbox"].curselection()
        if not selected_index:
            return

        skill_index = selected_index[0]
        self.current_skill_index = skill_index
        values = self.skills_data[skill_index]

        for i in range(54):
            self.ui["param_entries"][i].delete(0, tk.END)
            self.ui["param_entries"][i].insert(0, values[i])

    def select_last_skill(self):
        self.ui["skill_listbox"].select_clear(0, tk.END)
        self.ui["skill_listbox"].selection_set(tk.END)
        self.ui["skill_listbox"].activate(tk.END)
        self.on_skill_select(None)

    def edit_param_names(self):
        for i in range(54):
            new_name = simpledialog.askstring("參數名稱編輯", f"請輸入參數 {i+1} 的新名稱:", initialvalue=self.param_names[i])
            if new_name:
                self.param_names[i] = new_name
                self.ui["param_labels"][i].config(text=new_name)
        save_param_names(self.param_names)

if __name__ == "__main__":
    root = tk.Tk()
    app = SkillEditor(root)
    root.mainloop()
