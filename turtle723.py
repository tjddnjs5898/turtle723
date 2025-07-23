import serial
import time
import turtle


def connect_sensor(port='COM4', baud=9600):
    try:
        return serial.Serial(port, baud, timeout=1)
    except Exception as e:
        print(f"센서 연결 실패: {e}")
        return None


def read_distance(ser):
    try:
        if ser.in_waiting > 0:
            return float(ser.readline().decode().strip())
    except:
        pass
    return None


def out_of_bounds(t):
    x, y = t.pos()
    return abs(x) > 290 or abs(y) > 290


screen = turtle.Screen()
screen.setup(600, 600)
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)


def main():
    ser = connect_sensor('COM4')
    if not ser:
        return

    try:
        while True:
            d = read_distance(ser)
            if d:
                print(f"거리: {d} cm")
                if d < 10:
                    t.penup()
                else:
                    t.pendown()
                    t.forward(10)
                    if out_of_bounds(t):
                        t.left(180)
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        ser.close()
        turtle.bye()

main()
