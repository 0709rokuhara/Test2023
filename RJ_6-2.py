import glob
import json
import tkinter as tk

num1=[]
num2=[]

root = tk.Tk()
root.state('zoomed')

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

a=glob.glob('./kabeposter/*00_keypoints.json')
for n_value in a:
    with open(n_value, encoding='utf-8')as f:
        j=json.load(f)
        num1=(j['people'][0]['pose_keypoints_2d'])
        num2=(j['people'][1]['pose_keypoints_2d'])

# 線の描画
canvas.create_line(num1[6], num1[7], num1[3], num1[4], fill = "black", width = 3)
canvas.create_line(num1[3], num1[4], num1[15], num1[16], fill = "black", width = 3)
canvas.create_line(num2[6], num2[7], num2[3], num2[4], fill = "black", width = 3)
canvas.create_line(num2[3], num2[4], num2[15], num2[16], fill = "black", width = 3)
root.mainloop()