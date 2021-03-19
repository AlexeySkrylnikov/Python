from sys import argv


def salary(hours, rate, bonus):
    return hours * rate + bonus


worker_hours, worker_rate, worker_bonus = argv[1:]

print('Заработная плата сотрудника составит:',
      salary(hours=int(worker_hours), bonus=int(worker_bonus), rate=int(worker_rate)), 'р.')
