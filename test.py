import turtle as t  # 터틀모듈 불러오기
import random       #랜덤 모듈 불러오기
import time         #타임 모듈 불러오기
#클릭한 부분과 제일 거리가 가까운 카드 찾아줌
def find_card(x, y):    #클릭한 위치에서 가장 가까운 카드를 찾는 함수 정의
    min_idx = 0         #가장 가까운 카드 인덱스를 저장할 변수
    min_dis = 100       #최소 거리 저장하 변수

    for i in range(16): # 16개 카드 반복
        distance = turtles[i].distance(x, y) # 클릭한 위치와 카드 사이의 거리 계산
        if distance < min_dis:               # 위 거리가 최소 거리보다 작은가?
            min_dis = distance               # 작다면 최소 거리 갱신 & 가장 가까운 카드 인덱스 갱신
            min_idx = i
            
    # 카드를 클릭했을 경우에만 반환
    if min_dis < 50:        # 가장 가까운 카드와의 거리가 50보다 작은가?
        return min_idx      # 50보다 작을 시 해당 카드 인덱스 반환
    else:
        return None         # 50보다 크다면 None을 반환

def score_update(message):  # 점수와 시도 횟수 업데이트하는 함수 정의
    score_pen.clear()       # 기존에 화면에 표시된 내용 지움
    score_pen.write(f"{message}     {score}점/{attempt}번 시도", False, "center", ("", 15))
# 현재 점수, 시도 횟수를 화면 중앙에 글꼴 15크기로 표시

def result(message):        # 게임 결과 메세지를 화면에 표시하는 함수 정의
    t.goto(0, -60)          # 터틀을 (0, -60)좌표로 이동시킴
    t.write(message, False, "center", ("", 30, "bold"))
    # 주어진 메세지를 화면 중앙에 30폰트로 굵게 표시

def play(x, y):     # 플레이 함수 정의
    global click_num    # 클릭 횟수 저장하는 전역 변수
    global first_pick   # 첫 번째 클릭 카드의 인덱스 저장하는 전역 변수
    global second_pick  # 두 번째 클릭 카드의 인덱스 저장하는 전역 변수
    global attempt      # 시도 횟수 저장하는 전역 변수
    global score        # 점수 저장하는 전역 변수

    if attempt == 12:       # 시도 횟수가 12에 도달하면 
        result("Game Over") #  Game over 메세지 출력하고 게임 종료
    else:           # 12 미만일 때 
        card_idx = find_card(x, y) # 클릭한 위치에서 가장 가까운 카드 인덱스 찾음
        if card_idx is None or turtles[card_idx].shape() != default_img:
            return                 # 카드 인덱스가 None이거나 해당 카드가 기본 이미지가 아니면 함수 종료
        
        click_num += 1                              # 클릭 횟수 1 증가
        turtles[card_idx].shape(img_list[card_idx]) # 클릭한 카드 뒤집음

        if click_num == 1:          # 첫 번째 클릭인 경우
            first_pick = card_idx   # 첫 번째 클릭 카드 인덱스 저장
            
        elif click_num == 2:        # 두 번째 클릭인 경우 
            second_pick = card_idx  # 두 번째 클릭 카드 인덱스 저장
            click_num = 0           # 클릭 횟수 0으로 초기화
            attempt += 1            # 시도 횟수 1 증가

            if img_list[first_pick] == img_list[second_pick]:   # 두 카드의 이미지가 같다면
                score += 1              # 점수 1 증가
                score_update("정답")     # "정답" 메세지 출력
                
                if score == 8:          # 점수가 8이 되면 (모든 카드 매칭하면)
                    result("성공")       # "성공" 메세지 출력

            else:                       # 두 카드 이미지가 다르면
                score_update("오답")     # "오답" 메세지 출력
                t.ontimer(lambda: turtles[first_pick].shape(default_img), 1000)  # 1초 뒤 첫 번쨰 카드 원래대로 뒤집음
                t.ontimer(lambda: turtles[second_pick].shape(default_img), 1000) # 1초 뒤 두 번째 카드 원래대로 뒤집음

t.bgcolor("blue") # 배경색 파란색
t.setup(700, 700) # 창 크기 설정
t.up()            # 터틀 펜을 들어올려 이동할 때 그리지 않도록 설정
t.ht()            # 터틀을 숨김
t.goto(0, 280)    # 터틀을 화면 위쪽으로 이동시킴
t.write("카드 매칭 게임", False, "center", ("", 30, "bold"))  # 게임 이름 표시

# 점수 펜 설정
score_pen = t.Turtle() # 새로운 터틀 객체 생성 
score_pen.up()         # 펜 들어올려 이동할 때 그리지 않도록 설정
score_pen.ht()         # 터틀을 숨김
score_pen.goto(0, 230) # 점수 펜을 화면 위쪽으로 이동


turtles = [] # 터틀 객체 생성 및 배치 
pos_x = [-210, -70, 70, 210]  #x 좌표
pos_y = [-250, -110, 30, 170] #y 좌표

for x in range(4):          # x 좌표 반복
    for y in range(4):      # y 좌표 반복
        new_turtle = t.Turtle()  # 새로운 터틀 객체 생성           
        new_turtle.up()          # 펜 들어올려서 이동할 때 그리지 않도록 설정
        new_turtle.color("blue") # 터틀 색상 배경색과 같게하여 안 보이게 설정
        new_turtle.speed(0)      # 터틀 속도 최대로 설정
        new_turtle.goto(pos_x[x], pos_y[y]) # 터틀을 지정된 좌표로 이동
        turtles.append(new_turtle)          # 터틀 리스트에 추가

default_img = "gifs/default_img.gif"    # 기본 이미지 파일 경로
t.addshape(default_img)                 # 기본 이미지 등록

img_list = []                   # 이미지 리스트 생성
for i in range(8):              # 사진 총 8개, 8번 반복
    gif = f"gifs/img{i}.gif"    # 과일 이미지 파일 경로
    t.addshape(gif)             # 이미지 등록
    img_list.append(gif)        # 이미지 리스트에 추가
    img_list.append(gif)        # 이미지가 2개 씩 짝 지어 있어야 해서 이미지 한 번 더 추가

random.shuffle(img_list)            # 이미지들 랜덤하게 섞음
for i in range(16):                 #16번 반복
    turtles[i].shape(img_list[i])   #터틀에 이미지 설정

time.sleep(3)   # 3초간 앞면 보여줌

for i in range(16):  # 16번 반복
    turtles[i].shape(default_img) # 모든 터틀 이미지를 기본 이미지로 설정

click_num = 0       # 클릭 횟수 초기화    
score = 0           # 점수 초기화
attempt = 0         # 시도 횟수 초기화
first_pick = ""     # 첫 번째 선택 초기화
second_pick = ""    # 두 번째 선택 초기화

t.onscreenclick(play)  # 화면 클릭 이벤트 설정
t.done()               # 터틀 그래픽 메인 루프 시작
