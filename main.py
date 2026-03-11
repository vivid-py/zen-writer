import customtkinter as ctk 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("960x540")
        self.title("Zen Write")
        self.resizable(False, False)

app = App()
app.mainloop()
