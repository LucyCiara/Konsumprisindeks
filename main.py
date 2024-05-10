import matplotlib.pyplot as plt
import numpy as np

# A function for creating a dictionary variable based on the contents of a csv file.
def data_from_file_extraction(file_name: str) -> dict:
    with open(f"{file_name}", "r") as input_file:
        # Preparation of variables.
        temp_list = input_file.readlines()
        temp_list = [item.replace("\n", "").replace(",", ".").split(";") for item in temp_list]
        data_dict = {"År": [], "Årsgjennomsnitt": []}

        # Loop for creating the keys out of the name of each column.
        for item in temp_list[0][2:]:
            data_dict[f"{item}"] = []

        # Loop for filling the keys' lists with each column
        for row in temp_list[1:]:
            for i in range(len(row)):
                try:
                    data_dict[list(data_dict.keys())[i]].append(float(row[i].replace(",", "")))
                except:
                    data_dict[list(data_dict.keys())[i]].append(row[i].replace(",", ""))
    return data_dict

# A function for sorting through data_dict to find the element with the lowest value, it's column and its row, and returns the answer to the task.
def oppgave_1_lavest(data_dict: dict) -> str:
    # Creates a list of all the values in the dictionary, and sorts them based on size.
    konsumprisindeks_list = []
    for key in list(data_dict.keys())[2:]:
        for item in data_dict[key]:
            if item != ".":
                konsumprisindeks_list.append(item)
    konsumprisindeks_list = sorted(konsumprisindeks_list, key=float)

    # Finds the row and column of the lowest value, and prints out the answer to the task.
    for i in range(2, len(list(data_dict.keys()))):
        for j in range(len(data_dict["År"])):
            if data_dict[list(data_dict.keys())[i]][j] == konsumprisindeks_list[0]:
                return f"Lavest konsumprisindeks: {konsumprisindeks_list[0]}\nMåned: {list(data_dict.keys())[i]}\nÅr: {data_dict['År'][j]}"

# A function for sorting through data_dict to find the element with the highest value, it's column and its row, and returns the answer to the task.
def oppgave_1_høyest(data_dict: dict) -> str:
    # Creates a list of all the values in the dictionary, and sorts them based on size.
    konsumprisindeks_list = []
    for key in list(data_dict.keys())[2:]:
        for item in data_dict[key]:
            if item != ".":
                konsumprisindeks_list.append(item)
    konsumprisindeks_list = sorted(konsumprisindeks_list, key=float, reverse=True)

    # Finds the row and column of the highest value, and prints out the answer to the task.
    for i in range(2, len(list(data_dict.keys()))):
        for j in range(len(data_dict["År"])):
            if data_dict[list(data_dict.keys())[i]][j] == konsumprisindeks_list[0]:
                return f"Høyest konsumprisindeks: {konsumprisindeks_list[0]}\nMåned: {list(data_dict.keys())[i]}\nÅr: {data_dict['År'][j]}"

# A function for plotting values on a graph.
def oppgave_2_grafing(data_dict: dict):
    # Collects relevant values for the graph.
    tVerdier = [item for item in data_dict["År"]]
    fVerdier = [item for item in data_dict["Årsgjennomsnitt"]]
    
    # Various pyplot functions for displaying the graph.
    plt.plot(tVerdier, fVerdier)
    plt.gca().invert_yaxis()
    plt.title("Gjennomsnittlig konsumprisindeks over tid")
    plt.xlabel("$t$ (År)")
    plt.ylabel("$f$ (Gjennomsnittlig Konsumprisindeks)")
    plt.grid()
    plt.show()

# A function for plotting values on a bar diagram
def oppgave_2_stolpediagramgrafing(data_dict: dict, år: float):
    # Collects relevant values for the graph.
    måned = [item for item in list(data_dict.keys())[2:]]
    konsumprisindeks = [data_dict[item][data_dict["År"].index(år)] for item in list(data_dict.keys())[2:]]
    
    # Replaces each instance of "." with 0, because some values might not be logged, and to plot you need a number.
    for i in range(len(konsumprisindeks)):
        if konsumprisindeks[i] == ".":
            konsumprisindeks[i] = 0

    # Various pyplot functions for displaying the diagram.
    plt.bar(måned, konsumprisindeks)
    plt.title("Konsumerprisen hver måned i 2022")
    plt.grid()
    plt.show()

def oppgave_3_kalkulator(data_dict: dict, år1, år2, pris_år_A):
    år1 = float(år1)
    år2 = float(år2)
    pris_år_A = float(pris_år_A)

    index_for_år1 = data_dict["År"].index(år1)
    index_for_år2 = data_dict["År"].index(år2)
    pris_år_B = pris_år_A*data_dict["Årsgjennomsnitt"][index_for_år2]/data_dict["Årsgjennomsnitt"][index_for_år1]

    return f"Prisen vil i år {år2} være: {pris_år_B}"

# Prepares the variables.
file_name = "konsumprisindeks.csv"
data_dict = data_from_file_extraction(file_name)

# Prints out the answers to task 1.
print(oppgave_1_lavest(data_dict))
print(oppgave_1_høyest(data_dict))

# Plots the answers to task 2.
oppgave_2_grafing(data_dict)
oppgave_2_stolpediagramgrafing(data_dict, 2022.0)

# Prints out the answer to task 3.
startår = float(input("Skriv startsår:\n"))
sluttår = float(input("Skriv sluttår:\n"))
startpris = float(input("Skriv startspris:\n"))
print(oppgave_3_kalkulator(data_dict, startår, sluttår, startpris))