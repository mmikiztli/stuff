
# Report functions

def count_games(file_name):
    '''How many games are in the file?'''
    with open(file_name) as game_inv:
        return sum(1 for line in game_inv)

def decide(file_name, year):
    '''Is there a game from a given year?'''
    with open(file_name) as game_inv:
        for line in game_inv:
            if line.split("\t")[2] == str(year):
                return True
        return False

def get_latest(file_name):
    '''Which was the latest game?'''
    with open(file_name, "r") as game_inv:
        game_lines = game_inv.readlines()
    maximum = max(int(line.split("\t")[2]) for line in game_lines)
    for line in game_lines:
        if line.split("\t")[2] == str(maximum):
            return line.split("\t")[0]

def count_by_genre(file_name, genre):
    '''How many games do we have by genre?'''
    with open(file_name) as game_inv:
        return sum(1 for game_genre in [line.split("\t")[3] for line in game_inv] if game_genre == genre)

def get_line_number_by_title(file_name, title):
    '''What is the line number of the given game (by title)?'''
    with open(file_name) as game_inv:
        num = 0
        for line in game_inv:
            num += 1
            if line.split("\t")[0] == str(title):
                return num
        return "There is no game with this title."

def sort_abc(file_name):
    '''What is the alphabetical ordered list of the titles?'''
    with open(file_name, "r") as game_inv:
        game_lines = game_inv.readlines()
    titles = [x[0] for x in [line.split("\t") for line in game_lines]]
    for i in range(len(titles)):
        for j in range(len(titles)):
            if titles[i] < titles[j]:
                titles[i], titles[j] = titles[j], titles[i]
    return titles

def get_genres(file_name):
    '''What are the genres?'''
    with open(file_name) as game_inv:
        return sorted(set([line.split("\t")[3] for line in game_inv]), key = str.lower)

def when_was_top_sold_fps(file_name):
    '''What is the release date of the top sold "First-person shooter" game?'''
    game = open(file_name, "r")
    game_inv = game.readlines()
    game.close()
    genre = "First-person shooter"
    try:
        maximum = max(float(line.split("\t")[1]) for line in game_inv if line.split("\t")[3] == genre)
    except ValueError:
        return ("There is no %s" % genre)
    for line in game_inv:
        if line.split("\t")[3] == genre:
            if float(line.split("\t")[1]) == maximum:
                return int(line.split("\t")[2])
