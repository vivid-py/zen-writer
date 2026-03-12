from tkinter import Button
import customtkinter as ctk 
class appSettings(ctk.CTk):
    def __init__(self):
        super.init()
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.textboxFont=("Inter", 13)
        self.noteButtonTitleFont = ("Inter", 11)
        self.noteButtonTitles = []
        self.geometry("1920x1080")
        self.title("Zen Write")
        self.resizable(True, True)
        self.genTopMenu()
        self.genSidebar()
        self.genUI()
        self.text.bind("<KeyRelease>", self.getTitle)
    def genSidebar(self):
        self.sidebar = ctk.CTkScrollableFrame(self, width=200)
        self.sidebar._scrollbar.grid_forget()
        self.sidebar.pack(side="left", fill="y")
        self.btn1 = ctk.CTkButton(self.sidebar, text="New Note", fg_color="transparent", anchor="w", font=self.noteButtonTitleFont, border_color="#262626", border_width=2)
        self.btn1.pack(fill="x", padx=5, pady=5)
        self.noteButtonTitles.append(self.btn1)
    def genTopMenu(self):
        self.topBar = ctk.CTkFrame(self, height=30, fg_color="#2b2b2b")
        self.topBar.pack(side="top", fill="x")
        self.topBarSettingsButt = ctk.CTkButton(self.topBar, text="Settings", font=("Inter", 10, "bold"), fg_color="transparent", hover_color="darkgrey")
        self.topBarSaveFileButt = ctk.CTkButton(self.topBar, text="Save File", font=("Inter", 10, "bold"), fg_color="transparent", hover_color="darkgrey")
        self.topBarSaveFileButt.pack(side="left")
        self.topBarSettingsButt.pack(side="right")
    def genUI(self):
        self.text = ctk.CTkTextbox(self,width=760, height=510, font=self.textboxFont)
        self.text.pack(side="right", fill="both", expand=True)
    def getTitle(self, event=None):
        firstLine = self.text.get("1.0", "1.end")
        title = firstLine.strip() if firstLine.strip() else "New Note"
        if len(title) > 20:
            title = title[:17] + "..."
        if self.noteButtonTitles:
            self.noteButtonTitles[0].configure(text=title)   
app = App()
app.mainloop()
