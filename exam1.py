import tkinter as tk
from tkinter import ttk


def open_result_window(form_data):
    result_window = tk.Toplevel(root)
    result_window.title("Your Information")
    result_window.geometry("500x430")
    result_window.configure(bg="#140b1d")
    result_window.resizable(False, False)

    main_card = tk.Frame(result_window, bg="#25133a", padx=20, pady=20)
    main_card.pack(fill="both", expand=True, padx=20, pady=20)

    title = tk.Label(
        main_card,
        text="PERSONAL INTRODUCTION",
        fg="#ff5bd1",
        bg="#25133a",
        font=("Arial", 18, "bold")
    )
    title.pack(pady=(0, 18))

    details = [
        ("Name", form_data["name"]),
        ("Age", form_data["age"]),
        ("City", form_data["city"]),
        ("Hobby", form_data["hobby"]),
        ("Language", form_data["language"]),
    ]

    for label, value in details:
        row = tk.Frame(main_card, bg="#25133a", pady=8)
        row.pack(fill="x")

        tk.Label(row, text=f"{label}:", fg="#ff9ae6", bg="#25133a", font=("Arial", 12, "bold"), width=12, anchor="w").pack(side="left")
        tk.Label(row, text=value, fg="#f8ebff", bg="#25133a", font=("Arial", 12), anchor="w").pack(side="left", padx=10)

    close_btn = tk.Button(
        main_card,
        text="Close",
        bg="#ff5bd1",
        fg="#1d0828",
        font=("Arial", 12, "bold"),
        command=result_window.destroy,
        width=16,
        relief="flat",
        bd=0,
        cursor="hand2"
    )
    close_btn.pack(pady=(20, 0))


def submit_form():
    data = {
        "name": name_entry.get().strip(),
        "age": age_entry.get().strip(),
        "city": city_entry.get().strip(),
        "hobby": hobby_entry.get().strip(),
        "language": language_entry.get().strip(),
    }

    if not all(data.values()):
        status_label.config(text="Please fill all fields before submitting.", fg="#ff5555")
        return

    status_label.config(text="Submitted successfully!", fg="#7CFC00")
    open_result_window(data)


root = tk.Tk()
root.title("Personal Introduction Form")
root.geometry("530x620")
root.configure(bg="#120a1d")
root.resizable(False, False)

main_panel = tk.Frame(root, bg="#1d1230", padx=30, pady=30)
main_panel.pack(fill="both", expand=True)

header = tk.Label(
    main_panel,
    text="PERSONAL INTRODUCTION",
    fg="#ff5bd1",
    bg="#1d1230",
    font=("Arial", 22, "bold")
)
header.pack(pady=(0, 25))

form_frame = tk.Frame(main_panel, bg="#2b1a3d", padx=18, pady=20)
form_frame.pack(fill="both", expand=True)

fields = [
    ("Name", "name"),
    ("Age", "age"),
    ("City", "city"),
    ("Hobby", "hobby"),
    ("Language", "language"),
]

entries = {}
for label_text, key in fields:
    row = tk.Frame(form_frame, bg="#2b1a3d", pady=10)
    row.pack(fill="x")

    label = tk.Label(
        row,
        text=f"{label_text}:",
        width=12,
        anchor="w",
        fg="#ff9ae6",
        bg="#2b1a3d",
        font=("Arial", 11, "bold")
    )
    label.pack(side="left")

    entry = ttk.Entry(row, width=30, font=("Arial", 11))
    entry.pack(side="left", padx=(8, 0))
    entries[key] = entry

name_entry = entries["name"]
age_entry = entries["age"]
city_entry = entries["city"]
hobby_entry = entries["hobby"]
language_entry = entries["language"]

submit_btn = tk.Button(
    main_panel,
    text="Submit",
    bg="#ff5bd1",
    fg="#1d0828",
    font=("Arial", 12, "bold"),
    command=submit_form,
    width=18,
    relief="flat",
    bd=0,
    cursor="hand2"
)
submit_btn.pack(pady=20)

status_label = tk.Label(main_panel, text="", fg="#ffc7f2", bg="#1d1230", font=("Arial", 10, "bold"))
status_label.pack()

root.mainloop()