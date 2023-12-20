import matplotlib.pyplot as plt
import numpy as np
def get_time(marks, days):
    results = {}
    graph_mode = input("Would you like a graph as an output(y/n)")
    if graph_mode == "y":
        for subj, time in enumerate(marks):
            results[f"Subject {subj+1}"] = (round(((100 - marks[subj])/((100 * len(nums_ints)) - sum(marks))) * int(days), 1)) #+ " days"
        plt.bar(results.keys(), list(results.values()))
        plt.show()
    elif graph_mode == "n":
        for subj, time in enumerate(marks):
            results[f"Subject {subj + 1}"] = str(
                round(((100 - marks[subj]) / ((100 * len(nums_ints)) - sum(marks))) * int(days), 1)) + " days"
        return print("The distribution subjects is: " + str(results))

nums = input("Enter percentages: (without '%' symbol) ")
days_left = input("Enter the number of days left until next examination: ")
nums_ints = [eval(i) for i in list(nums.split(", "))]

try:
    results = get_time(nums_ints, days_left)
except TypeError:
    print("Error! Please use a space after the comma")
