win = open('correctReceiptNumb.txt').read().split()
mine = open('myReceiptNumb.txt').read().split()

print("中獎號碼:"),print( win)
print("我的號碼:"),print( mine)

for i, num in enumerate(mine):
    if num in win:
        print('第',i+1,'張發票對中號碼',num,  '!')
