import random
import time
import sys

#判断参数数量
if(len(sys.argv) < 2):
    print('您没有提供次数限制。')
    exit(1)

#限制次数
guess_limit = int(sys.argv[1])

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
        guess = int(input('这个数在0到100之间，请猜：'))
        if(guess == answer):
            is_right = True
            break
    
        if(guess < answer):
            print('你猜小了', end='，')
        else:
            print('你猜大了', end='，')
    
        if(i != guess_limit - 1):
            print('请继续猜。')
    #结束判断_____________________

    end_time = time.time()
    used_time = round(end_time - begin_time, 1)

    if(not(is_right)):
        print('你已经用完了所有机会', end='，')
    else:
        print('你猜对了', end='，')

    #记录成绩
    scores.append((cycle, is_right, used_time))

    print(f'游戏结束。共花时约{used_time}秒。')
    cont = input('要继续吗？(Y/N)\n').lower() == 'y'
    print('-----------------')

#显示成绩
for number, won, seconds in scores:
    won_text = '胜利' if won else '失败'
    print(f'第{number}局 {won_text} 用时{seconds}')