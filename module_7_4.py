team_1 = 'Мастера кода'
team_2 = 'Волшебники данных'

team1_num = 5
print('В команде Мастера кода участников: %d' % team1_num)

team2_num = 6
print('Итого сегодня в командах участников: %d и %d' % (team1_num, team2_num))

score_2 = 42
print('Команда Волшебники данных решила задач: {}'.format(score_2))

team1_time = 18015.2
team2_time = 2153.31451
print('Волшебники данных решили задачи за {} c'.format(team1_time))

score_1 = 40
print(f'Команды решили {score_1} и {score_2} задач')

challenge_result = 'победа'
print(f'Результат битвы: {challenge_result} команды {team_1}')

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')