# autoDetectReceipt
Auto detect two file , one of your number and another of receipt number  ,it will Automatically match prizes

win = open('correctReceiptNumb.txt').read().split()
mine = open('myReceiptNumb.txt').read().split()
#開啟你的兩個號碼txt檔


for i, num in enumerate(mine):
    if num in win:
        print('第',i+1,'張發票對中號碼',num,  '!')
#兩組號碼相互比對出中獎號碼
