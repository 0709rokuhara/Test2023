import glob
import json
import tkinter as tk

num1 = []
num2 = []
cnt = 0

root = tk.Tk()
root.state('zoomed')

# Canvasの作成
canvas = tk.Canvas(root, bg="white")
# Canvasを配置
canvas.pack(fill=tk.BOTH, expand=True)

born = [
    (0, 1), (0, 15), (0, 16), (15, 17),
    (16, 18), (2, 1), (2, 3), (3, 4),
    (1, 5), (5, 6), (6, 7), (1, 8),
    (9, 8), (8, 12), (9, 10), (10, 11),
    (11, 24), (11, 22), (22, 23), (12, 13),
    (13, 14), (14, 21), (14, 19), (19, 20),
]


def move():
    global cnt, num1, num2
    canvas.delete("all")

    if cnt < len(num1):
        point1 = num1[cnt]
        point2 = num2[cnt]

        for x in born:
            rx, ry = point1[x[0] * 3], point1[(x[0] * 3) + 1]
            sx, sy = point1[x[1] * 3], point1[(x[1] * 3) + 1]

            tx, ty = point2[x[0] * 3], point2[(x[0] * 3) + 1]
            ux, uy = point2[x[1] * 3], point2[(x[1] * 3) + 1]

            if rx>0 and ry>0 and sx>0 and sy>0:
                canvas.create_line(rx, ry, sx, sy, fill="black", width=3)
            if tx>0 and ty>0 and ux>0 and uy>0:
                canvas.create_line(tx, ty, ux, uy, fill="black", width=3)

    if cnt < len(num1) - 1:
        cnt += 1
    canvas.after(200, move)


a = glob.glob('./kabeposter/*')
for n_value in a:
    with open(n_value, encoding='utf-8') as f:
        j = json.load(f)
        num1.append(j['people'][0]['pose_keypoints_2d'])
        num2.append(j['people'][1]['pose_keypoints_2d'])

move()

root.mainloop()
