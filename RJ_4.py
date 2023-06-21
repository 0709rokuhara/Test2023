import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

# 線の描画
canvas.create_line(150, 150, 200, 190, fill = "black", width = 3)
canvas.create_line(150, 150, 100, 190, fill = "black", width = 3)
canvas.create_line(150, 150, 150, 65, fill = "black", width = 3)
canvas.create_line(150, 105, 200, 75, fill = "black", width = 3)
canvas.create_line(150, 105, 100, 75, fill = "black", width = 3)
canvas.create_oval(122, 5, 180, 65, width = 3)
root.mainloop()