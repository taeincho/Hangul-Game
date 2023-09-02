import os
print("[ HanGul-Game ]")
print("1) Start")
ch = input(">")
if ch == "1":
    os.system("cls")
    print("대한민국 만세이며 뒷자리 사람은 이시형이다.")
    ch = input(">")
    if ch == "대한민국 만세이며 뒷자리 사람은 이시형이다.":
        print("성공")
    else:
        print("실패")