
# Report functions

TITLE = 0
SOLD = 1
YEAR = 2
GENRE = 3
PUBLISHER = 4

def read_games(file_name):
    with open(file_name) as game_inv:
        game_lines = game_inv.readlines()
    return [line.split("\t") for line in game_lines]

def count_games(file_name):
    '''How many games are in the file?'''
    games = read_games(file_name)
    return len(games)

def decide(file_name, year):
    '''Is there a game from a given year?'''
    games = read_games(file_name)
    for game in games:
        if game[YEAR] == str(year):
            return True
    return False

def get_latest(file_name):
    '''Which was the latest game?'''
    games = read_games(file_name)
    maximum = max(int(game[YEAR]) for game in games)
    for game in games:
        if game[YEAR] == str(maximum):
            return game[TITLE]

def count_by_genre(file_name, genre):
    '''How many games do we have by genre?'''
    games = read_games(file_name)
    return sum(1 for game in games if game[GENRE] == genre)

def get_line_number_by_title(file_name, title):
    '''What is the line number of the given game (by title)?'''
    games = read_games(file_name)
    num = 0
    for game in games:
        num += 1
        if game[TITLE] == str(title):
            return num
    return "There is no game with this title."

def sort_abc(file_name):
    '''What is the alphabetical ordered list of the titles?'''
    games = read_games(file_name)
    titles = [game[TITLE] for game in games]
    for i in range(len(titles)):
        for j in range(len(titles)):
            if titles[i] < titles[j]:
                titles[i], titles[j] = titles[j], titles[i]
    return titles

def get_genres(file_name):
    '''What are the genres?'''
    games = read_games(file_name)
    return sorted(set([game[GENRE] for game in games]), key = str.lower)

def when_was_top_sold_fps(file_name, genre = "First-person shooter"):
    '''What is the release date of the top sold "First-person shooter" game?'''
    games = read_games(file_name)
    try:
        maximum = max(float(game[SOLD]) for game in games if game[GENRE] == genre)
    except ValueError:
        return ("There is no %s" % genre)
    for game in games:
        if game[GENRE] == genre:
            if float(game[SOLD]) == maximum:
                return int(game[YEAR])
