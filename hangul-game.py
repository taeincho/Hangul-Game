import os, random
from time import sleep
list = [
    "대한민국 만세이며 뒷자리 사람은 이시형이다.",
    "깃허브는 허브이며, 허브는 풀떼기입니다.",
    "크롬은 구글에서 제작한 인터넷 브라우저 입니다.",
    "크로미움은 구글에서 제작한 오픈소스 인터넷 브라우저 입니다.",
    "이시형은 컴퓨터를 잘 합니다(반어법)"
    "The world is world."
    "The face is the 싸이언쓰"
    "Minecraft the best!!!!!@!@!!!1004minecraft!!!1"
    "khonichiwa!(해석:안녕하세요!)일본어입니다."
    "Helloba!"
    "NiCeN Meets yoyu"
]



print("[ HanGul-Game ] 추신: '헿헿ㅎ게'는 쓰지 마세요.")
print("1) Start")
ch = input(">")

if ch == "1":
    os.system("cls")
def main():
    os.system("cls")
    word = random.choice(list)
    print(word)
    ch = input(">")
    if ch == word:
        print("성공")
        sleep(2)
        main()
    else:
        print("실패")
        sleep(2)
        main()
main()
