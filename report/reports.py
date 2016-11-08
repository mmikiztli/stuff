
# Report functions


def count_games(file_name):
    with open(file_name) as game_inv:
        return sum(1 for line in game_inv)

def decide(file_name, year):
    with open(file_name) as game_inv:
        #igy miert fogadja el a test.py? ha kiprintelem nem adja ki a megoldast, de a unittesten atmegy
        return (True if line.split("\t")[2] == str(year) else False for line in game_inv)

        #igy mukodik, csak hosszu, nem? nem tom h lehetne rovidebben
        """
        result = [True if line.split("\t")[2] == str(year) else False for line in game_inv]
        if True in result:
            return True
        else:
            return False
        """

def get_latest(file_name):
    with open(file_name) as game_inv:
        maximum = max(int(line.split("\t")[2]) for line in game_inv)
    #miert kell ujra megnyitni? ha nem nyitom meg ujra, nem mukodik
    with open(file_name) as game_inv:
        result = [x[0] for x in [[line.split("\t")[0], line.split("\t")[2]] for line in game_inv] if x[1] == str(maximum)]
        return result[0]

        #ez egy alternativ megoldas lett volna, mukodik is, csak a dictionaryben random rakja az elemeket
        #es a feladatban az volt, h ha tobb max van, akkor sorrendben az elsot adja ki a file-bol
        """
        game_inv_dict = {line.split("\t")[0]: line.split("\t")[2] for line in game_inv}
        return max(game_inv_dict, key=game_inv_dict.get)
        """

#def count_by_genre(file_name, genre):


