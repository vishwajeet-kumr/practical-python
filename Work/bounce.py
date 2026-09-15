# bounce.py
#
# Exercise 1.5

height_of_tower = 100
count_bounces = 0
bounces_till = 3/5
final_result = bounces_till * height_of_tower

while  count_bounces < 10:
    print(round(final_result, 4))
    final_result = final_result*bounces_till
    count_bounces += 1
