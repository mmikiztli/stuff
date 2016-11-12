import reports

game_file = "game_stat.txt"

print (reports.count_games(game_file))
print (reports.decide(game_file,2000))
print (reports.get_latest(game_file))
print (reports.count_by_genre(game_file,"First-person shooter"))
print (reports.get_line_number_by_title(game_file,"Counter-Strike"))
print (reports.sort_abc(game_file))
print (reports.get_genres(game_file))
print (reports.when_was_top_sold_fps(game_file))