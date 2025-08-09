import tkinter as tk
from tkinter import messagebox


contacts = []  # This will store our contacts in memory


def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    
    if name == "" or phone == "" or email == ""  :
        messagebox.showwarning("Warning", "Please fill all fields!")
        return
    
    contacts.append({"name": name, "phone": phone, "email": email})
    update_listbox()
    entry_name.delete(0, tk.END)
    entry_phone.delete (0, tk.END)
    entry_email.delete (0, tk.END)
    messagebox.showinfo  ("Success", f"Contact '{name}' added!")

def update_listbox() :
    listbox_contacts.delete(0, tk.END)
    for contact in contacts :
        listbox_contacts.insert (tk.END, f"{contact['name']} - {contact['phone']} - {contact['email']}")

def delete_contact() :
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a contact to delete!")
        return
    
    index = selected[0]
    contact_name = contacts[index]['name']
    del  contacts[index]
    update_listbox()
    messagebox.showinfo("Deleted", f"Contact '{contact_name}' deleted!")

def search_contact():
    query = entry_search.get().lower()
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']} - {contact['email']}")
    entry_search.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Info Book")
root.geometry("500x400")


tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root, width=50)
entry_name.pack()

tk.Label(root, text="Phone:").pack()
entry_phone = tk.Entry(root, width=50)
entry_phone.pack()

tk.Label (root, text="Email:").pack()
entry_email = tk.Entry(root, width=50)
entry_email.pack()


tk.Button (root, text="Add Contact", command=add_contact, bg="lightgreen").pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact, bg="lightcoral").pack(pady=5)


tk.Label(root, text="Search:").pack()
entry_search = tk.Entry(root, width=50)
entry_search.pack()
tk.Button (root, text="Search Contact", command=search_contact, bg="lightblue").pack(pady=5)


listbox_contacts = tk.Listbox(root, width=60, height=10)
listbox_contacts.pack(pady=10)


root.mainloop()   # Start the app//
