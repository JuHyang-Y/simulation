import turtle
t = turtle.Turtle()
t.shape("turtle")

#값 입력 받기(문자열 -> 상수)
s1 = turtle.textinput("","왼쪽 하단 모서리 좌표 x, y : ")
n1 = s1.split(' ')
x = list(map(int, n1))
s2 = turtle.textinput("","오른쪽 상단 모서리 좌표 x, y : ")
n2 = s2.split(' ')
y = list(map(int, n2))
s3 = turtle.textinput("","점의 좌표 x, y : ")
n3 = s3.split(' ')
z = list(map(int, n3))


#거북이로 좌표가지고 사각형그리기
t.penup()
t.goto(x[0], x[1])
t.pendown()
t.goto(y[0], x[1])
t.goto(y[0], y[1])
t.goto(x[0], y[1])
t.goto(x[0], x[1])
#입력좌표로 이동
t.penup()
t.goto(z[0], z[1])
t. pendown()

#사각형 안에 좌표가 있을 때와 없을 때
if (x[0] <= z[0] <= y[0] and x[1] <= z[1] <= y[1]) :
    #좌표 점 그리기
    t.color("black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    #출력
    t.write("점은 사각형의 내부에 있습니다.")
else :
    #좌표 점 그리기
    t.color("black")
    t.begin_fill()
    t.circle(10)
    #출력
    t.end_fill()
    t.write("점은 사각형의 외부에 있습니다.")


turtle.done()
turtle.bye
