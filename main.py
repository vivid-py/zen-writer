import customtkinter as ctk 
class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        self.textboxFont=("Inter", 13)
        self.noteButtonTitleFont = ("Inter", 11, "bold")
        self.noteButtonTitles = []
        self.geometry("960x540")
        self.title("Zen Write")
        self.resizable(False, False)
        self.genSidebar()
        self.genUI()
        self.text.bind("<KeyRelease>", self.getTitle)
    def genSidebar(self):
        self.sidebar = ctk.CTkScrollableFrame(self, height=540, width=200)
        self.sidebar._scrollbar.grid_forget()
        self.sidebar.pack(side="left")
        self.btn1 = ctk.CTkButton(self.sidebar, text="New Note", fg_color="transparent", anchor="w", font=self.noteButtonTitleFont)
        self.btn1.pack(fill="x", padx=5, pady=5)
        self.noteButtonTitles.append(self.btn1)
    def genUI(self):
        self.header1 = 0
        self.text = ctk.CTkTextbox(self,width=760, height=540, font=self.textboxFont)
        self.text.pack()
    def getTitle(self, event=None):
        firstLine = self.text.get("1.0", "1.end")
        title = firstLine.strip() if firstLine.strip() else "New Note"
        if len(title) > 20:
            title = title[:17] + "..."
        if self.noteButtonTitles:
            self.noteButtonTitles[0].configure(text=title)



    
app = App()
app.mainloop()
