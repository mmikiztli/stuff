import reports
# Export functions

functions = [reports.count_games("game_stat.txt"),
             reports.decide("game_stat.txt",2000),
             reports.get_latest("game_stat.txt"),
             reports.count_by_genre("game_stat.txt","First-person shooter"),
             reports.get_line_number_by_title("game_stat.txt","Counter-Strike"),
             reports.sort_abc("game_stat.txt"),
             reports.get_genres("game_stat.txt"),
             reports.when_was_top_sold_fps("game_stat.txt")]


def export(source_file_name,output_file_name):
    reports_export = open(output_file_name, "w+")
    for item in functions:
        reports_export.writelines(item.__doc__ + "\n" + str(item) + "\n")
    reports_export.close()

"""def export(source_file_name,output_file_name):
    reports_export = open(output_file_name, "w+")
    reports_export.writelines(reports.count_games.__doc__ + "\n" + str(reports.count_games(source_file_name)) + "\n")
    reports_export.writelines(str(reports.decide(source_file_name,2000))+ "\n")
    reports_export.writelines(str(reports.get_latest(source_file_name))+ "\n")
    reports_export.writelines(str(reports.count_by_genre(source_file_name,"First-person shooter"))+ "\n")
    reports_export.writelines(str(reports.get_line_number_by_title(source_file_name,"Counter-Strike"))+ "\n")
    reports_export.writelines(str(reports.sort_abc(source_file_name))+ "\n")
    reports_export.writelines(str(reports.get_genres(source_file_name))+ "\n")
    reports_export.writelines(str(reports.when_was_top_sold_fps(source_file_name)))
    reports_export.close()"""

export("game_stat.txt","reports.txt")