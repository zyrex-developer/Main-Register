import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("400x350")
app.title("Register Account")

# Title
title = ctk.CTkLabel(app, text="Register Account", font=("Arial", 22, "bold"))
title.pack(pady=20)

# Username
username = ctk.CTkEntry(app, placeholder_text="Username", width=250)
username.pack(pady=10)

# Password
password = ctk.CTkEntry(app, placeholder_text="Password", show="*", width=250)
password.pack(pady=10)

# Message
message = ctk.CTkLabel(app, text="")
message.pack(pady=5)

# Show/Hide password
def toggle_password():
    if password.cget("show") == "":
        password.configure(show="*")
    else:
        password.configure(show="")

show_btn = ctk.CTkButton(app, text="Show Password", command=toggle_password, width=150)
show_btn.pack(pady=5)

# 🔹 REGISTER
def register():
    user = username.get().strip()
    pwd = password.get().strip()

    if not user or not pwd:
        message.configure(text="Fill all fields ❌", text_color="red")
        return

    with open("users.txt", "a") as file:
        file.write(user + "," + pwd + "\n")

    message.configure(text="Register success ✅", text_color="green")

    username.delete(0, "end")
    password.delete(0, "end")
    
    
    # Button Register
register_btn = ctk.CTkButton(app, text="Register", command=register, width=200)
register_btn.pack(pady=5)

app.mainloop()