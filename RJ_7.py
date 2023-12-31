import os

class_labels = {
    0: "person",
    1: "bicycle",
    2: "car",
    3: "motorcycle",
    4: "airplane",
    5: "bus",
    6: "train",
    7: "truck",
    8: "boat",
    9: "traffic light",
    10: "fire hydrant",
    11: "stop sign",
    12: "parking meter",
    13: "bench",
    14: "bird",
    15: "cat",
    16: "dog",
    17: "horse",
    18: "sheep",
    19: "cow",
    20: "elephant",
    21: "bear",
    22: "zebra",
    23: "giraffe",
    24: "backpack",
    25: "umbrella",
    26: "handbag",
    27: "tie",
    28: "suitcase",
    29: "frisbee",
    30: "skis",
    31: "snowboard",
    32: "sports ball",
    33: "kite",
    34: "baseball bat",
    35: "baseball glove",
    36: "skateboard",
    37: "surfboard",
    38: "tennis racket",
    39: "bottle",
    40: "wine glass",
    41: "cup",
    42: "fork",
    43: "knife",
    44: "spoon",
    45: "bowl",
    46: "banana",
    47: "apple",
    48: "sandwich",
    49: "orange",
    50: "broccoli",
    51: "carrot",
    52: "hot dog",
    53: "pizza",
    54: "donut",
    55: "cake",
    56: "chair",
    57: "couch",
    58: "potted plant",
    59: "bed",
    60: "dining table",
    61: "toilet",
    62: "tv",
    63: "laptop",
    64: "mouse",
    65: "remote",
    66: "keyboard",
    67: "cell phone",
    68: "microwave",
    69: "oven",
    70: "toaster",
    71: "sink",
    72: "refrigerator",
    73: "book",
    74: "clock",
    75: "vase",
    76: "scissors",
    77: "teddy bear",
    78: "hair drier",
    79: "toothbrush"
}

folder_path = "labels"
#指定したディレクトリ内のファイル名のリスト取得
file_list = os.listdir(folder_path)
file_list.sort()
#各クラスが表示されたかどうか調べるため
visited_classes = set()

for filename in file_list:
    file_path = os.path.join(folder_path, filename)
    with open(file_path, "r") as file:
        #ファイルのすべての行をリストとして読み込みます
        lines = file.readlines()
        #linesの各行についてループ
        for line in lines:
            #行の先頭と末尾の空白文字消去
            line = line.strip()
            if line: #空の行でないとき
                class_id = int(line.split()[0]) #整数に変換、先頭要素を取得
                #ラベルの重複がないようにする
                if class_id in class_labels and class_id not in visited_classes:
                    class_name = class_labels[class_id] #クラス名を取得し、格納
                    print(class_name)
                    visited_classes.add(class_id)
