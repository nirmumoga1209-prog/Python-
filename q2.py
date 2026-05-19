my_list = [10, 20, 30]       

my_list.append(40)         # [10, 20, 30, 40]
my_list.insert(1, 15)      # [10, 15, 20, 30, 40]
my_list.remove(20)         # [10, 15, 30, 40]
my_list.pop()              # [10, 15, 30]
my_list.reverse()          # [30, 15, 10]

print("Final list:", my_list)