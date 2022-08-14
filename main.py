import random
import time
import sys

#判断参数数量
if (len(sys.argv) < 2):
    print('您没有提供次数限制。')
    exit(1)

#限制次数
try:
    guess_limit = int(sys.argv[1])
except ValueError:
    print("给定的参数必须是整数。")
    exit(1)

cont = True
scores = []
cycle = 0

while cont:
    cycle += 1
    answer = random.randint(0, 100)
    is_right = False
    begin_time = time.time()

    #开始判断_____________________
    for i in range(guess_limit):
        try:
            guess = int(input('这个数在0到100之间，请猜：'))
        except ValueError:
            print('输入值不能被转换为整数型，请检查是否有输入错误。')
            exit(1)
        if (guess == answer):
            is_right = True
            break

        if (guess < answer):
            print('你猜小了', end='，')
        else:
            print('你猜大了', end='，')

        if (i != guess_limit - 1):
            print('请继续猜。')
    #结束判断_____________________

    end_time = time.time()
    used_time = round(end_time - begin_time, 1)

    if (not (is_right)):
        print('你已经用完了所有机会', end='，')
    else:
        print('你猜对了', end='，')

    #记录成绩
    scores.append((cycle, is_right, used_time))

    print(f'游戏结束。共花时约{used_time}秒。')
    cont = input('要继续吗？(Y/N)\n').lower() == 'y'
    print('-----------------')

#过滤列表
filtered = list(filter(lambda x: x[1], scores))
if (len(filtered) != 0):
    best_score = min(filtered, key=lambda x: x[2])[2]
else:
    best_score = 0

#显示成绩
for number, won, seconds in scores:
    won_text = '胜利' if won else '失败'
    label = ''
    if (won and seconds == best_score):
        label = '[最佳]'
    print(f'第{number}局 {won_text} 用时{seconds}{label}')
