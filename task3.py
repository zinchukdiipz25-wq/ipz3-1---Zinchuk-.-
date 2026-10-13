N = 5
events = [f"подія {i}" for i in range(1, 9)]   # потік із 8 подій

buffer = [None] * N
next_pos = 0     # комірка, у яку писати наступного разу
count = 0        # скільки подій збережено (до N)

for event in events:
    buffer[next_pos] = event
    next_pos = (next_pos + 1) % N    # дійшли до кінця — починаємо з нуля
    if count < N:
        count += 1

start = next_pos if count == N else 0   # найстарша подія
for i in range(count):
    print(buffer[(start + i) % N])
