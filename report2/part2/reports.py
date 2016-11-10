import math
# Report functions

def get_most_played(file_name):
    game = open("game_stat.txt", "r")
    game_inv = game.readlines()
    game.close()
    maximum = max(float(line.split("\t")[1]) for line in game_inv)
    for line in game_inv:
        if float(line.split("\t")[1]) == maximum:
            return line.split("\t")[0]

def sum_sold(file_name):
    with open(file_name) as game_inv:
        return sum(float(x[1]) for x in [line.split("\t") for line in game_inv])

def get_selling_avg(file_name):
    game = open("game_stat.txt", "r")
    game_inv = game.readlines()
    game.close()
    count = sum(1 for line in game_inv)
    return sum(float(line.split("\t")[1]) for line in game_inv) / count

def count_longest_title(file_name):
    with open(file_name) as game_inv:
        return len(max((x[0] for x in [line.split("\t") for line in game_inv]), key = len))

def get_date_avg(file_name):
    game = open("game_stat.txt", "r")
    game_inv = game.readlines()
    game.close()
    count = sum(1 for line in game_inv)
    return math.ceil(sum(int(line.split("\t")[2]) for line in game_inv) / count)

def get_game(file_name, title):
    game = open("game_stat.txt", "r")
    game_inv = game.readlines()
    game.close()
    game_rows = [x for x in [line.strip("\n").split("\t") for line in game_inv] if x[0] == title]
    game_rows = game_rows[0] #flatten
    game_rows[1] = float(game_rows[1]) #ha nem float?
    game_rows[2] = int(game_rows[2])
    return game_rows

def count_grouped_by_genre(file_name):
    game = open("game_stat.txt", "r")
    game_inv = game.readlines()
    game.close()
    keys = []
    values = []
    genres = [keys.append(x[3]) for x in [line.split("\t") for line in game_inv] if x[3] not in keys]
    for i in keys:
        count = 0
        for line in game_inv:
            line = line.split("\t")
            if i == line[3]:
                count += 1
        values.append(count)
    return dict(zip(keys, values))

def get_date_ordered(file_name):
    game = open("game_stat.txt", "r")
    game_inv = game.readlines()
    game.close()
    ordered = [[x[2], x[0]] for x in [line.split("\t") for line in game_inv]]
    ordered = sorted(ordered, reverse = True)
    for i in range(len(ordered)):
        for n in range(1,len(ordered)):
            if ordered[i][0] == ordered[n][0]:
                if ordered[i][1] < ordered[n][1]:
                    ordered[i], ordered[n] = ordered[n], ordered[i]
    return [x[1] for x in ordered]