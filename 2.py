seconds = int(input('Specify the time in seconds: '))

hours = (seconds % 86400) // 3600
minutes = (seconds % 3600) // 60
seconds %= 60

if hours < 10:
    hours = '0'+str(hours)
else:
    hours = str(hours)

if minutes < 10:
    minutes = '0'+str(minutes)
else:
    minutes = str(minutes)

if seconds < 10:
    seconds = '0'+str(seconds)
else:
    seconds = str(seconds)

print(f'HH:MM:SS time is {hours}:{minutes}:{seconds}')
