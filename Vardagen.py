Dagu = [
    'gibba',
    'äta chips',
    'sova',
    'gråta i sängen'
]
import random

dag = 0
dagar = ['mon','tue','wed','thu','fre','sat','sun']


for i in range(0, 7):
    print(f"--{dagar[dag].capitalize()}--")
    Daga = random.randint(0, len(Dagu)-1)
    print(f"{Dagu[Daga].capitalize()}")
    dag +=1