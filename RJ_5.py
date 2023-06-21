import tkinter as tk

root = tk.Tk()
root.geometry("800x300")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

# 線の描画
line1=canvas.create_line(150, 150, 200, 190, fill = "black", width = 3)
line2=canvas.create_line(150, 150, 100, 190, fill = "black", width = 3)
line3=canvas.create_line(150, 150, 150, 65, fill = "black", width = 3)
line4=canvas.create_line(150, 105, 200, 75, fill = "black", width = 3)
line5=canvas.create_line(150, 105, 100, 75, fill = "black", width = 3)
circle1=canvas.create_oval(122, 5, 180, 65, width = 3)

def move():
    canvas.move(line1, 10, 0)
    canvas.move(line2, 10, 0)
    canvas.move(line3, 10, 0)
    canvas.move(line4, 10, 0)
    canvas.move(line5, 10, 0)
    canvas.move(circle1, 10, 0)
    canvas.after(80, move)

def clk():
    move()

buttun = tk.Button(root, text="アニメーションスタート", command=clk)
buttun.pack()

root.mainloop()