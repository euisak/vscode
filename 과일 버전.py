import turtle as t #터틀모듈 그래픽 불러오기
import random #랜덤 모듈 불러오기
import time #타임 모듈 불러오기

def find_card(x, y):    #클릭한 부분과 제일 거리가 가까운 카드 찾아줌
    min_idx = 0
    min_dis = 100

    for i in range(16):
        distance = turtles[i].distance(x, y)
        if distance < min_dis:
            min_dis = distance
            min_idx = i
    return min_idx            

def score_update(m):
    score_pen.clear()
    score_pen.write(f"{m}     {score}점/{attempt}번 시도", False, "center", ("", 15))

def result(m):
    t.goto(0, -60)
    t.write(m, False, "center", ("", 30, "bold"))

def play(x, y):
    global click_num
    global first_pick
    global second_pick
    global attempt
    global score

    if attempt == 12: #시도 회수가 12번이 되면 게임 오버
        result("Game Over")
        

    else:
        click_num +=1 # 한번 클릭 할 때 마다 click num이 하나 씩 증가
        card_idx = find_card(x, y)
        turtles[card_idx].shape(img_list[card_idx]) #클릭한 사진 보여줌

        if click_num == 1: #클릭 횟수가 1이라면 클릭한 카드의 인덱스를 first pick에 넣어둠
            first_pick = card_idx
        elif click_num == 2:  #클릭 횟수가 2이라면 클릭한 카드의 인덱스를 second pick에 넣어둠
            second_pick = card_idx
            click_num = 0 # 매 2회 마다 클릭 값 초기화
            attempt += 1 #시도회수 증가

            if img_list[first_pick] == img_list[second_pick]: #둘의 경로가 같다면
                score += 1 # 스코어 증가
                score_update("정답")
                if score == 8: #모든 그림 다 맞추면 성공 뜨도록
                    result("성공")
                    
            else:
                score_update("오답") # 둘의 경로가 다르다면 오답
                turtles[first_pick].shape(default_img) #오답인 경우 다시 default img로 돌아가게 하여 뒤집어줌
                turtles[second_pick].shape(default_img)





t.bgcolor("blue") #배경화면 색 설정
t.setup(700,700) #캔버스 크기 설정
t.up()
t.ht()
t.goto(0, 280) #제목 위치
t.write("카드 매칭 게임", False, "center", ("", 30, "bold"))

# 점수 펜 객체 생성  
score_pen = t.Turtle()
score_pen.up()
score_pen.ht()
score_pen.goto(0, 230)


#터틀 객체 생성
turtles = [] #리스트 만들어서 관리
pos_x = [-210, -70, 70, 210] # 터틀 위치 시킬 x 좌표
pos_y = [-250, -110, 30, 170] # 터틀 위치 시킬 y 좌표(제목이 위치할 곳을 고려하여 40정도 내려서 사용)

for x in range(4):
    for y in range(4):
        new_turtle = t.Turtle() #new turtle에 담아줌
        new_turtle.up() #펜 기능 사용하지 않아 들어줌
        new_turtle.color("blue") #배경색과 같게 하여 준비 과정 안 보이게함
        new_turtle.speed(0) # 최대 속도로 설정
        new_turtle.goto(pos_x[x], pos_y[y]) #x y 좌표값으로 이동 시켜줌
        turtles.append(new_turtle)

default_img = "gifs/default_img.gif" #이미지라는 폴더 안에 default_img라고 저장되어있는 파일
t.addshape(default_img) #이렇게 사용하는 것 비효율 적이라 for문 이용하여 불러줄거임

img_list = []
for i  in range(8):
    gif = f"gifs/img{i}.gif"
    t.addshape(gif)
    img_list.append(gif)
    img_list.append(gif)  #카드 매칭 위해서 같은 사진을 2개씩 맞춰서 넣어줘야하기 때문에

random.shuffle(img_list) #img_list에 담긴 사진들을 섞어줌
for i in range(16):
    turtles[i].shape(img_list[i]) 

time.sleep(3) #이미지 3초간 보여주고 defult 이미지(빈 사진)으로 바꿔줌

for i in range(16):
    turtles[i].shape(default_img)

click_num = 0 #  클릭 횟수 변수(매 2회 클릭마다 정답체크)
score = 0 # 점수 변수
attempt = 0 #시도한 횟수 변수
first_pick = "" # 첫 번째 클릭한 이미지
second_pick = "" # 두 번째 클릭한 이미지

t.onscreenclick(play)
t.done()
 
