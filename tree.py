import turtle
import matplotlib.pyplot as plt
import multiprocessing

# Carbon emissions data (in millions of tons) for the last 10 years
years = list(range(2013, 2023))
carbon_emissions = [1000, 950, 900, 850, 800, 750, 700, 650, 600, 550]  # Sample data

# Measures to reduce carbon emissions
measures = {
    'Increase the use of renewable energy sources': 0.15,
    'Energy efficiency': 0.1,
    'Sustainable transport': 0.1,
    'Reforestation': 0.05,
}

# Function to calculate emission reductions
def reduce_emissions(emissions, measures):
    for measure, reduction in measures.items():
        emissions *= (1 - reduction)
        print(f'After applying the measure "{measure}", carbon emissions are: {emissions:.2f} million tons')
    return emissions

# Data visualization
def plot_carbon_emissions():
    plt.figure(figsize=(10, 5))
    plt.plot(years, carbon_emissions, marker='o', label='Carbon Emissions')
    plt.title('Carbon Emissions Over the Last 10 Years')
    plt.xlabel('Year')
    plt.ylabel('Carbon Emissions (million tons)')
    plt.xticks(years)
    plt.grid()
    plt.legend()
    plt.show()

# Drawing a tree
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
    # Apply measures and calculate new emissions
    current_emissions = carbon_emissions[-1]
    print(f'\nCurrent carbon emissions: {current_emissions} million tons')
    new_emissions = reduce_emissions(current_emissions, measures)
    print(f'\nNew carbon emissions after applying measures: {new_emissions:.2f} million tons')
    
    # Start visualization and tree drawing in separate processes
    plot_process = multiprocessing.Process(target=plot_carbon_emissions)
    draw_process = multiprocessing.Process(target=draw_tree)
    plot_process.start()
    draw_process.start()
    plot_process.join()
    draw_process.join()