import tkinter as tk
from tkinter import ttk
from typing import Optional

"""
omg.py - Tkinter application class starter

Run:
    python omg.py
"""


class App(tk.Tk):
    """Simple Tkinter application skeleton using a class-based structure."""

    def __init__(self, title: str = "Tkinter App", size: str = "800x600") -> None:
        super().__init__()
        self.title(title)
        self.geometry(size)

        # Optional state
        self._status_text = tk.StringVar(value="Ready")

        # Build UI
        self._create_menu()
        self._create_toolbar()
        self._create_main()
        self._create_statusbar()

        # Bindings
        self.bind("<Control-q>", lambda e: self.quit())
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def _create_menu(self) -> None:
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label="New", command=self.on_new)
        file_menu.add_command(label="Open...", command=self.on_open)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_close)
        menubar.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menubar, tearoff=False)
        help_menu.add_command(label="About", command=self.on_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.config(menu=menubar)

    def _create_toolbar(self) -> None:
        toolbar = ttk.Frame(self, padding=(2, 2))
        btn_new = ttk.Button(toolbar, text="New", command=self.on_new)
        btn_open = ttk.Button(toolbar, text="Open", command=self.on_open)
        btn_new.pack(side="left", padx=2)
        btn_open.pack(side="left", padx=2)
        toolbar.pack(side="top", fill="x")

    def _create_main(self) -> None:
        # Main content area - replace with your widgets/layout
        main_frame = ttk.Frame(self, padding=(8, 8))
        label = ttk.Label(main_frame, text="Hello, Tkinter!", font=("Segoe UI", 14))
        label.pack(anchor="center", expand=True)
        sample_button = ttk.Button(main_frame, text="Click me", command=self.on_click)
        sample_button.pack(pady=10)
        main_frame.pack(fill="both", expand=True)

    def _create_statusbar(self) -> None:
        status = ttk.Frame(self, relief="sunken")
        lbl = ttk.Label(status, textvariable=self._status_text, anchor="w")
        lbl.pack(fill="x", padx=4)
        status.pack(side="bottom", fill="x")

    # Event handlers / actions -------------------------------------------------
    def set_status(self, text: str, timeout: Optional[int] = 3000) -> None:
        """Set status text; optionally clear after timeout milliseconds."""
        self._status_text.set(text)
        if timeout:
            self.after_cancel(getattr(self, "_status_after_id", None))
            self._status_after_id = self.after(timeout, lambda: self._status_text.set(""))

    def on_new(self) -> None:
        self.set_status("New action triggered", 2000)

    def on_open(self) -> None:
        self.set_status("Open action triggered", 2000)

    def on_about(self) -> None:
        tk.messagebox.showinfo("About", "Tkinter App - Starter template")

    def on_click(self) -> None:
        self.set_status("Button clicked", 1500)

    def on_close(self) -> None:
        # place cleanup logic here
        self.destroy()


if __name__ == "__main__":
    app = App(title="OMG - Tkinter Starter")
    app.mainloop()