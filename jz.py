import tkinter as tk
from tkinter import filedialog
from jzd import jzd
import time
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()
out='界址点检查结果%s.txt'%time.time()
j=jzd.Jzd(path,out)
j.run()