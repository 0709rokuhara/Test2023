import glob

nums=[]
a=glob.glob('./sample/*[13579]_kgu.txt')
for n_value in a:
    with open(n_value, encoding='utf-8')as file:
        try:
            y=int(file.readline())
            nums.append(y)
        except ValueError:
            continue
print(sum(nums))
