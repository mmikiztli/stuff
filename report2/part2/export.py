import reports
# Export functions

def export(source_file_name,output_file_name):
    reports_export = open(output_file_name, "w+")
    reports_export.writelines("What is the title of the most played game?:" + "\n")
    reports_export.writelines(reports.get_most_played(source_file_name) + "\n")
    reports_export.writelines("How many copies have been sold total?:" + "\n")
    reports_export.writelines(str(reports.sum_sold(source_file_name))+ "\n")
    reports_export.writelines("What is the average selling?:" + "\n")
    reports_export.writelines(str(reports.get_selling_avg(source_file_name))+ "\n")
    reports_export.writelines("How many characters long is the longest title?:" + "\n")
    reports_export.writelines(str(reports.count_longest_title(source_file_name))+ "\n")
    reports_export.writelines("What is the average of the release dates?:" + "\n")
    reports_export.writelines(str(reports.get_date_avg(source_file_name))+ "\n")
    reports_export.writelines("What properties has a game?:" + "\n")
    reports_export.writelines(str(reports.get_game(source_file_name,"Counter-Strike"))+ "\n")
    reports_export.writelines("How many games are there grouped by genre?:" + "\n")
    reports_export.writelines(str(reports.count_grouped_by_genre(source_file_name))+ "\n")
    reports_export.writelines("What is the date ordered list of the games?:" + "\n")
    reports_export.writelines(reports.get_date_ordered(source_file_name))
    reports_export.close()

export("game_stat.txt","reports.txt")