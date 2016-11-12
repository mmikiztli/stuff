
class Game:

    def __init__(self, title, sold, year, genre, publisher):
        self.title = str(title)
        self.sold = float(sold)
        self.year = int(year)
        self.genre = str(genre)
        self.publiser = str(publisher)

class GameInventory:

    def __init__(self, file_name):
        self.fileName = file_name

    def read(self):
        with open(self.fileName) as game_inv:
            game_lines = game_inv.readlines()
        return [Game(*line.split("\t")) for line in game_lines]

class Reporter:

    def __init__(self, inventory):
        self.games = inventory.read()

    def countGames(self):
        return len(self.games)

    def decide(self, year):
        for game in self.games:
            if game.year == int(year):
                return True
        return False

    def getLatest(self):
        maximum = max(int(game.year) for game in self.games)
        for game in self.games:
            if game.year == maximum:
                return game.title

    def countByGenre(self, genre):
        return sum(1 for game in self.games if game.genre == str(genre))

    def getLineNumberByTitle(self, title):
        num = 0
        for game in self.games:
            num += 1
            if game.title == str(title):
                return num
        return "There is no game with this title."

    def sortAbc(self):
        titles = [game.title for game in self.games]
        for i in range(len(titles)):
            for j in range(len(titles)):
                if titles[i] < titles[j]:
                    titles[i], titles[j] = titles[j], titles[i]
        return titles

    def getGenres(self):
        return sorted(set([game.genre for game in self.games]), key = str.lower)

    def whenWasTopSoldFps(self, genre="First-person shooter"):
        try:
            maximum = max(game.sold for game in self.games if game.genre == genre)
        except ValueError:
            return ("There is no %s" % genre)
        for game in self.games:
            if game.genre == genre and game.sold == maximum:
                    return game.year


# Boilerplate code for unit tests

def count_games(file_name):
    '''How many games are in the file?'''
    return Reporter(GameInventory(file_name)).countGames()

def decide(file_name, year):
    '''Is there a game from a given year?'''
    return Reporter(GameInventory(file_name)).decide(year)

def get_latest(file_name):
    '''Which was the latest game?'''
    return Reporter(GameInventory(file_name)).getLatest()

def count_by_genre(file_name, genre):
    '''How many games do we have by genre?'''
    return Reporter(GameInventory(file_name)).countByGenre(genre)

def get_line_number_by_title(file_name, title):
    '''What is the line number of the given game (by title)?'''
    return Reporter(GameInventory(file_name)).getLineNumberByTitle(title)

def sort_abc(file_name):
    '''What is the alphabetical ordered list of the titles?'''
    return Reporter(GameInventory(file_name)).sortAbc()

def get_genres(file_name):
    '''What are the genres?'''
    return Reporter(GameInventory(file_name)).getGenres()

def when_was_top_sold_fps(file_name):
    '''What is the release date of the top sold "First-person shooter" game?'''
    return Reporter(GameInventory(file_name)).whenWasTopSoldFps()

