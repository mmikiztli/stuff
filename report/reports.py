
from sys import maxsize

# Report functions


def count_games(file_name):
    with open(file_name) as game_inv:
        return sum(1 for line in game_inv)

def decide(file_name, year):
    with open(file_name) as game_inv:
        #igy miert fogadja el a test.py? ha kiprintelem nem adja ki a megoldast, de a unittesten atmegy
        # azert mert a test.py nem teljes, csak egyetlenegy peldara nezi (year=2000)
        # return (line.split("\t")[2] == str(year) for line in game_inv)
        # igy jobb mert nem nezi vegig, ha nem muszaj:
        for line in game_inv:
            if line.split("\t")[2] == str(year):
                return True
        return False

            #igy mukodik, csak hosszu, nem? nem tom h lehetne rovidebben
        """
        result = [True if line.split("\t")[2] == str(year) else False for line in game_inv]
        if True in result:
            return True
        else:
            return False
        """

def get_latest(file_name):
    #with open(file_name) as game_inv:
    #    maximum = max(int(line.split("\t")[2]) for line in game_inv)
    #miert kell ujra megnyitni? ha nem nyitom meg ujra, nem mukodik
    #azert mert a for line in game_env-vel vegigolvasod mar egyszer
    # nem lehet tobbszor vegigmenni rajta egy megnyitassal
    with open(file_name) as game_inv:
        # result = [x[0] for x in [[line.split("\t")[0], line.split("\t")[2]] for line in game_inv] if x[1] == str(maximum)]
        # return result[0]

        # sokkal jobbat nem tudok, mint direktbe vegigszamolni, azaz:
        (latest_game, latest_year) = (None, -maxsize-1)  # assume dinos didn't write computer games
        for line in game_inv:
            game_prop = line.split("\t")
            (game, year) = (game_prop[0], int(game_prop[2]))
            if year > latest_year:
                (latest_game, latest_year) = (game, year)
        return latest_game

        #ez egy alternativ megoldas lett volna, mukodik is, csak a dictionaryben random rakja az elemeket
        #es a feladatban az volt, h ha tobb max van, akkor sorrendben az elsot adja ki a file-bol
        """
        game_inv_dict = {line.split("\t")[0]: line.split("\t")[2] for line in game_inv}
        return max(game_inv_dict, key=game_inv_dict.get)
        """


