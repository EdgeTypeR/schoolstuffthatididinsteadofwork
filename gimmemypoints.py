#pip install tkinter simpledialog messagebox pandas ha véletlenül nem futna le
#a GUI részt egy régi projektből hasznosítottam át
#a pandas excel mókolást most találtam ki :p
#az excel-t mindig felülírja mentéskor

import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import pandas as pd

class GroupManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Csoportkezelő")
        
        self.groups = {}

        self.label = tk.Label(root, text="Csoportok kezelése", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.add_group_button = tk.Button(root, text="Új csoport hozzáadása", command=self.add_group)
        self.add_group_button.pack(pady=5)

        self.add_person_button = tk.Button(root, text="Személy hozzáadása csoporthoz", command=self.open_add_person_window)
        self.add_person_button.pack(pady=5)

        self.show_groups_button = tk.Button(root, text="Csoportok megtekintése", command=self.show_groups)
        self.show_groups_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Mentés Excel fájlba", command=self.save_to_excel)
        self.save_button.pack(pady=5)

    def add_group(self):
        group_name = simpledialog.askstring("Csoport neve", "Add meg a csoport nevét:")
        if group_name:
            if group_name not in self.groups:
                self.groups[group_name] = []
                messagebox.showinfo("Siker", f"A(z) '{group_name}' csoport létrehozva.")
            else:
                messagebox.showwarning("Hiba", "Ez a csoport már létezik.")

    def open_add_person_window(self):
        if not self.groups:
            messagebox.showwarning("Hiba", "Nincsenek létrehozott csoportok.")
            return

        # Új ablak létrehozása
        add_person_window = tk.Toplevel(self.root)
        add_person_window.title("Személy hozzáadása csoporthoz")
        add_person_window.geometry("300x150")

        label = tk.Label(add_person_window, text="Válassz egy csoportot:")
        label.pack(pady=10)

        group_selector = ttk.Combobox(add_person_window, state="readonly", values=list(self.groups.keys()))
        group_selector.pack(pady=5)
        group_selector.current(0)

        def add_person():
            group_name = group_selector.get()
            if group_name:
                person_name = simpledialog.askstring("Személy neve", "Add meg a személy nevét:", parent=add_person_window)
                if person_name:
                    self.groups[group_name].append(person_name)
                    messagebox.showinfo("Siker", f"A(z) '{person_name}' hozzáadva a(z) '{group_name}' csoporthoz.")
                    add_person_window.destroy()
            else:
                messagebox.showwarning("Hiba", "Kérlek, válassz egy csoportot.")

        add_button = tk.Button(add_person_window, text="Hozzáadás", command=add_person)
        add_button.pack(pady=10)

    def show_groups(self):
        groups_info = ""
        for group, people in self.groups.items():
            groups_info += f"Csoport: {group}\nTagok: {', '.join(people) if people else 'Nincsenek tagok'}\n\n"
        
        if groups_info:
            messagebox.showinfo("Csoportok", groups_info)
        else:
            messagebox.showinfo("Csoportok", "Nincsenek létrehozott csoportok.")

    def save_to_excel(self):
        max_members = max((len(people) for people in self.groups.values()), default=0)
        data = {group: people + [""] * (max_members - len(people)) for group, people in self.groups.items()}
        df = pd.DataFrame(data)

        try:
            df.to_excel("csoportok.xlsx", index=False)
            messagebox.showinfo("Siker", "A csoportok mentve lettek a 'csoportok.xlsx' fájlba.")
        except Exception as e:
            messagebox.showerror("Hiba", f"Hiba történt a mentés során: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GroupManagerApp(root)
    root.mainloop()
