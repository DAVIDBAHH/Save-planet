import turtle
import matplotlib.pyplot as plt
import multiprocessing

# Дані про запаси деревини (в мільйонах кубічних метрів) за останні 12 років
роки = list(range(2013, 2025))
запаси_деревини = [300, 320, 310, 330, 340, 350, 360, 370, 380, 390, 400, 410]  # Приклад даних

# Function to visualize wood stock
def plot_wood_stock():
    plt.figure(figsize=(10, 5))
    plt.plot(роки, запаси_деревини, marker='o', label='Запас деревини')
    plt.title('Запас деревини в лісах України з 2013 по 2024 рік')
    plt.xlabel('Рік')
    plt.ylabel('Запас деревини (мільйони кубічних метрів)')
    plt.xticks(роки)
    plt.grid()
    plt.legend()
    plt.show()

# Function to draw a tree
def draw_tree():
    tu = turtle.Turtle()
    tu.goto(0, -300)
    tu.screen.bgcolor("black")
    tu.pensize(2)
    tu.color("green")
    tu.left(90)
    tu.backward(100)
    tu.speed(0)

    def tree(i):
        if i < 10:
            return
        else:
            tu.forward(i)
            tu.color("blue")
            tu.circle(2)
            tu.color("green")
            tu.left(30)
            tree(3 * i / 4)
            tu.right(60)
            tree(3 * i / 4)
            tu.left(30)
            tu.backward(i)

    tree(200)
    turtle.done()

if __name__ == '__main__':
    # Запуск візуалізації та малювання дерева в окремих процесах
    process_plot = multiprocessing.Process(target=plot_wood_stock)
    process_draw = multiprocessing.Process(target=draw_tree)
    process_plot.start()
    process_draw.start()
    process_plot.join()
    process_draw.join()
