from player import Player
from playerreader import PlayerReader

def filter_by_nationality_FIN(player: Player, nation: str):
    return player.nationality == nation

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.players = reader.get_players()
    
    def top_scorers_by_nationality(self, nation: str):
        filteredPlayers = filter(lambda x: filter_by_nationality_FIN(x, nation), self.players)
        filteredPlayers = list(filteredPlayers)
        filteredPlayers.sort(key=lambda x: x.points, reverse=True)
        return filteredPlayers