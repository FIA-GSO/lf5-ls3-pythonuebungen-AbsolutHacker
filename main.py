# This is a sample Python script.
# Press Umschalt+F10 to execute it or replace it with your code.

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#---------------------Aufgabe 1 ------------------------------------
def compute_r2d2_population(steps: int) -> tuple[int,int,int]:
    """
        Computes the r2d2 population for the given step amount
    :param steps: amount of steps to compute the population (e.g.: 5)
    :return: tuple of children, adults, and old r2d2s
    """
    population = (10, 10, 10)
    while steps > 0:
        population = population_step(population)
        steps -= 1
    return population

def population_step(population: tuple[int, int, int]) -> tuple[int, int, int]:
    """
    :param population: tuple of (young, adult, old) r2d2s
    :return: tuple of (young, adult, old) r2d2s after applying reproduction and aging
    """
    young = population[1] * 4 + population[2] * 2
    adult = population[0] // 2
    old = population[1] // 3
    return (young, adult, old)

#---------------------Aufgabe 2 Streichholz------------------------------
#IMPLEMENT YOUR SOLUTION FOR THE STREICHHOLZSPIEL HERE
def player_draw(num_matches):
    print()
    _input = int(input(f"There are {num_matches} matches left. How many do you draw? "))
    if _input > 0 and _input <= min(6, num_matches):
        return _input
    else:
        print("*** ERROR: Invalid draw! ***")
        return player_draw(num_matches)

def run_nim():
    # player A draws
    print(f"The computer drew 2 matches. There are 29 matches remaining.")
    num_matches = 29
    while num_matches > 0:
        # player B draws
        _player_draw = player_draw(num_matches)
        num_matches -= _player_draw
        print(f"You drew {_player_draw} matches. There are {num_matches} matches remaining.")
        if num_matches == 0:
            break
        # player A draws
        npc_draw = 7 - _player_draw
        num_matches -= npc_draw
        print(f"The computer drew {npc_draw} matches. There are {num_matches} matches remaining.")
    print("You lost!")

#---------------------Aufgabe 3 Heron ------------------------------------
def abweichung(a: float, b: float) -> float:
    return abs(a - b)

def mittelwert(a: float, b: float) -> float:
    return (a + b) / 2

def heron_step(x: float, a: float, b: float) -> tuple[float, float]:
    a = mittelwert(a, b)
    b = x / a
    return (a, b)

def heron_verfahren(area : float, threshold:float) -> float:
    """
        computes the square root using the heron method
    :param area: size of the area e.g.25
    :param threshold: threshold for the heron method e.g. 0.01
    :return:the square root of the given area according to the heron method
    """
    laenge_a, laenge_b = area, 1.0
    while abweichung(laenge_a, laenge_b) >= threshold:
        laenge_a, laenge_b = heron_step(area, laenge_a, laenge_b)
    return laenge_a


#---------------------Aufgabe 4 Quersumme------------------------------
#IMPLEMENT, IF NECESSARY, EXERCISE 4 HERE BUT USE A FUNCTION!
def digit_sum(numerator: int) -> int:
    sum = 0
    while numerator > 0:
        sum += (numerator % 10)
        numerator //= 10
    return sum

#---------------MANAGEMENT----------------------
#-------------COMMENT/UNCOMMENT lines to launch the different exercises
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("You need to adjust this code to run your implementation")

    # Aufgabe 1
    print(f"""
        # R2D2 Population after 5 steps is: 
        # Young: {compute_r2d2_population(5)[0]}
        # Adults: {compute_r2d2_population(5)[1]}
        # Old: {compute_r2d2_population(5)[2]}""")
    # print (compute_r2d2_population(5))

    # Aufgabe 2
    run_nim()

    # Aufgabe 3
    print (f"Die Wurzel für die Fläche 25 und Grenze 0.01 nach Heron ist: {heron_verfahren(25, 0.01)}")

    # Aufgabe 4
    number = int(input("Geben Sie eine ganze Zahl ein: "))
    print(f"Die Quersumme der Zahl {number} ist {digit_sum(number)}.")

    # Use a breakpoint in the code line below to debug your script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
