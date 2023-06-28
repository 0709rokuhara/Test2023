import glob
import json
num1=[]
num2=[]
a=glob.glob('./kabeposter/*00_keypoints.json')
for n_value in a:
    with open(n_value, encoding='utf-8')as f:
        j=json.load(f)
        num1=(j['people'][0]['pose_keypoints_2d'])
        num2=(j['people'][1]['pose_keypoints_2d'])
print('1人目：x座標', num1[0], 'y座標', num1[1], '信頼度', num1[2])
print('2人目：x座標', num2[0], 'y座標', num2[1], '信頼度', num2[2])