grades = {"Ahmed":[83,67,56],"Saad":[76,78,89],"Zahid":[99,87,67]}

result_list = [(key, sum(values) / len(values)) for key, values in grades.items()]
print(result_list)


multiples_of_5 = {x: x ** 2 for x in range(5, 105, 5)}
print(multiples_of_5)

keys = ["ali", "ahmed", "asrhs"]
values = ["12","12","13"]
zipped = zip(keys,values)
color_dict = dict(zipped)


sorted_color_dict = dict(sorted(color_dict.items(), reverse=True))
print(sorted_color_dict)

footballer_goals = {"Eusebio":120, "Cruyff":104,"Pele":150, "Ronaldo":132,"Messi":125,"Maradona":170}
goals = {x: y for x,y in footballer_goals.items() if y >= 130}
print(goals)