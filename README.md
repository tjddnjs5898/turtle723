# 초음파 센서에 따른 거북이 제어
- 초음파 센서로 장애물을 감지하면 직진하던 거북이가 멈춘다.
- 거북이가 창의 벽에 닿으면 방향을 반대로 바꿔 이동.

### 필요한 모듈 가져오기
- import serial      # 초음파 센서와 시리얼 통신용
- import time        # 일정 시간 대기 (0.5초 간격)
- import turtle      # 그래픽으로 거북이 움직임 표현

### 센서 연결 함수
- def connect_sensor(port='COM4', baud=9600):
-  try:
-  return serial.Serial(port, baud, timeout=1)  #시리얼 연결 시도
-   except Exception as e:
-   print(f"센서 연결 실패: {e}")  #연결 실패 시 에러 출력
-   return None

### 거리 읽는 함수
- def read_distance(ser):
-    try:
-  if ser.in_waiting > 0:  # 읽을 데이터가 있으면
-   return float(ser.readline().decode().strip())  # 거리값 읽어서 실수형 변환
-    except:
-   pass
-    return None

### 화면 경계를 넘었는지 확인하는 함수
- def out_of_bounds(t):
-  x, y = t.pos()
-  return abs(x) > 290 or abs(y) > 290

### 화면 및 거북이 초기화
- screen = turtle.Screen()
- screen.setup(600, 600)  # 600x600 픽셀 크기의 창

- t = turtle.Turtle()
- t.shape("turtle")       # 거북이 모양 지정
- t.speed(1)              # 움직임 속도 (1은 느림)

### <코드>
- #초음파 거리에 따른 거북이 이동구현
- #벽에 닿으면 돌아감

- import serial
- import time
- import turtle


- def connect_sensor(port='COM4', baud=9600):
- try:
- return serial.Serial(port, baud, timeout=1)
- except Exception as e:
- print(f"센서 연결 실패: {e}")
- return None

- def read_distance(ser):
- try:
- if ser.in_waiting > 0:
- return float(ser.readline().decode().strip())
- except:
- pass
- return None

- def out_of_bounds(t):
- x, y = t.pos()
- return abs(x) > 290 or abs(y) > 290

- screen = turtle.Screen()
- screen.setup(600, 600)
- t = turtle.Turtle()
- t.shape("turtle")
- t.speed(1)

- def main():
- ser = connect_sensor('COM4')
- if not ser:
- return

- try:
- while True:
- d = read_distance(ser)
- if d:
- print(f"거리: {d} cm")
- if d < 10:
- t.penup()
- else:
- t.pendown()
- t.forward(10)
- if out_of_bounds(t):
- t.left(180)
- time.sleep(0.5)
- except KeyboardInterrupt:
- pass
- finally:
- ser.close()
- turtle.bye()
- main()



