with open("hoge.txt", "r") as f:
    data = f.read(100) # 1つながりのstr型として最初の100文字を読み込む    
for i in data:         # str型をイテレータにすると、1文字ずつ取り出す
    print(i)
