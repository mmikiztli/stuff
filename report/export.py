import reports

identity = lambda x: str(x)
list_printer = lambda l: "\n".join([str(e) for e in l])

functions = [[reports.count_games, [], identity],
             [reports.decide, [2000], identity],
             [reports.get_latest, [], identity],
             [reports.count_by_genre, ["First-person shooter"], identity],
             [reports.get_line_number_by_title, ["Counter-Strike"], identity],
             [reports.sort_abc, [], list_printer],
             [reports.get_genres, [], list_printer],
             [reports.when_was_top_sold_fps, [], identity]
             ]

def export(source_file_name, output_file_name):
    with open(output_file_name, "w+") as reports_export:
        for [function, params, printer] in functions:
            reports_export.writelines(function.__doc__ + "\n" + printer(function(source_file_name, *params)) + "\n\n")


export("game_stat.txt", "reports.txt")
