import turtle as t
import random
import time

t.bgcolor("blue") #배경화면 색 설정
t.setup(700,700)
t.up()
t.ht()
t.goto(0, 280)
t.write("카드 매칭 게임", False, "center", ("", 30, "bold"))

#터틀 객체 생성
turtles = []
pos_x = [-210, -70, 70, 210]
pos_y = [-250, -110, 30, 170]

for x in range(4):
    for y in range(4):
        new_turtle = t.Turtle()
        new_turtle.up()
        new_turtle.color("blue") #배경색과 같게 하여 준비 과정 안 보이게함
        new_turtle.speed(0)
        new_turtle.goto(pos_x[x], pos_y[y])
        turtles.append(new_turtle)

default_img = "gifs/default_img.gif" #이미지라는 폴더 안에 default_img라고 저장되어있는 파일
t.addshape(default_img) #이렇게 사용하는 것 비효율 적이라 for문 이용하여 불러줄거임

img_list = []
for i  in range(8):
    gif = f"gifs/img{i}.gif"
    t.addshape(gif)
    img_list.append(gif)
    img_list.append(gif)  #카드 매칭 위해서 같은 사진을 2개씩 맞춰서 넣어줘야하기 때문에

random.shuffle(img_list)
for i in range(16):
    turtles[i].shape(img_list[i]) 
