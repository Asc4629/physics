import csv

data = [["Shah","Male",114000.00],["Vats"," Male",65000.00],["Vats","Female",43150.00],["Kumar", "Female ",69500.00],
        ["Vats", "Female", 155000.00],["Kumar","Male", 103000.00],["Shah", "Male" ,55000.00],
        ["Shah", "Female", 112400.00],["Kumar","Female",81030.00],["Vats", "Male", 71900.00]]

with open('data10.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)