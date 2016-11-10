import reports
# Printing functions

print (reports.get_most_played("game_stat.txt"))
print (reports.sum_sold("game_stat.txt"))
print (reports.get_selling_avg("game_stat.txt"))
print (reports.count_longest_title("game_stat.txt"))
print (reports.get_date_avg("game_stat.txt"))
print (reports.get_game("game_stat.txt","Counter-Strike"))
print (reports.count_grouped_by_genre("game_stat.txt"))
print (reports.get_date_ordered("game_stat.txt"))

