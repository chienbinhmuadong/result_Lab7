import matplotlib.pyplot as plt
import pandas as pd

time = []
throttle_position = []
air_mass_flow = []


file = pd.read_csv("D:/nam nhat/term2/Programming/lab7/data1.csv", encoding="cp1251", delimiter = ";")
time = file['Время']
throttle_position = file['Положение дроссельной заслонки (%)']
air_mass_flow = file['Массовый расход воздуха (кг\ч)']


def graph():
# график зависимости Положения дроссельной заслонки от времени
    plt.subplot(1,2,1)
    plt.plot(time, throttle_position, color = 'blue')
    plt.xlim([0,50])
    plt.ylim([0, 200])
    plt.title("depend of throttle position on time")
    plt.xlabel("Time (s)")
    plt.ylabel("throttle position (%)")
# график зависимости Массового расхода воздуха от времени
    plt.subplot(1, 2, 2)
    plt.plot(time, air_mass_flow, color = "red")
    plt.xlim([0, 50])
    plt.ylim([0, 400])
    plt.title("denpend of air mass flow on time")
    plt.xlabel("Time (s)")
    plt.ylabel("air mass flow (kg/h)")
    plt.show()


# график корреляции
def correlation():
    plt.scatter(throttle_position, air_mass_flow, color = "green")
    plt.xlim([0, 200])
    plt.ylim([0, 400])
    plt.title("коррелация")
    plt.xlabel("Положение дроссельной заслонки (%)")
    plt.ylabel("Массовый расход воздуха (кг\ч)")
    plt.show()

graph()
correlation()