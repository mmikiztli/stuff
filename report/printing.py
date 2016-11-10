import reports
# Printing functions

print (reports.count_games("game_stat.txt"))
print (reports.decide("game_stat.txt",2000))
print (reports.get_latest("game_stat.txt"))
print (reports.count_by_genre("game_stat.txt","First-person shooter"))
print (reports.get_line_number_by_title("game_stat.txt","Counter-Strike"))
print (reports.sort_abc("game_stat.txt"))
print (reports.get_genres("game_stat.txt"))
print (reports.when_was_top_sold_fps("game_stat.txt"))