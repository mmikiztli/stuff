import reports
# Export functions

def export(source_file_name,output_file_name):
    reports_export = open(output_file_name, "w+")
    reports_export.writelines("How many games are in the file?:" + "\n")
    reports_export.writelines(str(reports.count_games(source_file_name)) + "\n")
    reports_export.writelines("Is there a game from a given year?:" + "\n")
    reports_export.writelines(str(reports.decide(source_file_name,2000))+ "\n")
    reports_export.writelines("Which was the latest game?:" + "\n")
    reports_export.writelines(str(reports.get_latest(source_file_name))+ "\n")
    reports_export.writelines("How many games do we have by genre?:" + "\n")
    reports_export.writelines(str(reports.count_by_genre(source_file_name,"First-person shooter"))+ "\n")
    reports_export.writelines("What is the line number of the given game (by title)?:" + "\n")
    reports_export.writelines(str(reports.get_line_number_by_title(source_file_name,"Counter-Strike"))+ "\n")
    reports_export.writelines("What is the alphabetical ordered list of the titles?:" + "\n")
    reports_export.writelines(str(reports.sort_abc(source_file_name))+ "\n")
    reports_export.writelines("What are the genres?:" + "\n")
    reports_export.writelines(str(reports.get_genres(source_file_name))+ "\n")
    reports_export.writelines("What is the release date of the top sold 'First-person shooter' game?:" + "\n")
    reports_export.writelines(str(reports.when_was_top_sold_fps(source_file_name)))
    reports_export.close()

export("game_stat.txt","reports.txt")