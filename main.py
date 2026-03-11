import customtkinter as ctk 
class App(ctk.CTk):
    textboxFont=("Inter", 13)
    def __init__(self):
        super().__init__()
        self.geometry("960x540")
        self.title("Zen Write")
        self.resizable(False, False)
        self.genSidebar()
        self.genUI()
    def genSidebar(self):
        self.sidebar = ctk.CTkScrollableFrame(self, height=540, width=200)
        self.sidebar._scrollbar.grid_forget()
        self.sidebar.pack(side="left")
    def genUI(self):
        self.text = ctk.CTkTextbox(self,width=760, height=540, font=self.textboxFont).pack()
    
app = App()
app.mainloop()
