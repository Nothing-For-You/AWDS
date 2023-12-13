def get_time(marks, days):
    results = {}
    for subj, time in enumerate(marks):
        results[f"Subject {subj+1}"] = str(round(((100 - marks[subj])/((100 * len(nums_ints)) - sum(marks))) * int(days), 1)) + " days"
    return print("The distribution subjects is: " + str(results))


nums = input("Enter percentages: (without '%' symbol) ")

"Please use proper punctuation, with a space after the comma"
days_left = input("Enter the number of days left until next examination: ")



nums_ints = [eval(i) for i in list(nums.split(", "))]

try:
    get_time(nums_ints, days_left)
except TypeError:
    print("Error! Please use a space after the comma")

