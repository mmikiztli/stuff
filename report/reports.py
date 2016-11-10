
# Report functions


def count_games(file_name):
    with open(file_name) as game_inv:
        return sum(1 for line in game_inv)

def decide(file_name, year):
    with open(file_name) as game_inv:
        for line in game_inv:
            if line.split("\t")[2] == str(year):
                return True
        return False

def get_latest(file_name):
    game = open("game_stat.txt", "r")
    game_inv = game.readlines()
    game.close()
    maximum = max(int(line.split("\t")[2]) for line in game_inv)
    for line in game_inv:
        if line.split("\t")[2] == str(maximum):
            return line.split("\t")[0]

def count_by_genre(file_name, genre):
    with open(file_name) as game_inv:
        return sum(1 for x in [line.split("\t") for line in game_inv] if x[3] == genre)

def get_line_number_by_title(file_name, title):
    with open(file_name) as game_inv:
        num = 0
        for line in game_inv:
            num += 1
            if line.split("\t")[0] == str(title):
                return num

def sort_abc(file_name):
    game = open("game_stat.txt", "r")
    game_inv = game.readlines()
    game.close()
    titles = [x[0] for x in [line.split("\t") for line in game_inv]]
    sorted = []
    for i in range(len(titles)):
        for n in range(len(titles)):
            if titles[i] >= titles[n]:
                titles[i] = titles[i]
            else:
                titles[i], titles[n] = titles[n], titles[i]
    return titles

def get_genres(file_name):
    with open(file_name) as game_inv:
        genres_list = []
        genres = [genres_list.append(x[3]) for x in [line.split("\t") for line in game_inv] if x[3] not in genres_list]
        return sorted(genres_list, key = str.lower)

def when_was_top_sold_fps(file_name):
    game = open("game_stat.txt", "r")
    game_inv = game.readlines()
    game.close()
    try:
        maximum = max(float(line.split("\t")[1]) for line in game_inv if line.split("\t")[3] == "First-person shooter")
    except ValueError:
        return ("There is no First-person shooter")
    for line in game_inv:
        if line.split("\t")[3] == "First-person shooter":
            if float(line.split("\t")[1]) == maximum:
                return int(line.split("\t")[2])


