



class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1, n+1))
        print(f"New starting player is: {players[0]}")
        return rec_helper(players, k, 0)

def num_players_left(players):
    return len(players)

def rec_helper(players, moves, first_player_idx):

    if num_players_left(players) == 1:
        return players[0]
    
    curr_player_to_remove_idx = first_player_idx
    index_of_player_to_remove = first_player_idx + moves - 1
    if index_of_player_to_remove < num_players_left(players):
        print(f"From the following players that left: {players}")
        removed_player = players.pop(index_of_player_to_remove)
        print(f"We just removed the following player: {removed_player}")
        next_first_player_idx = index_of_player_to_remove % num_players_left(players) 
        print(f"New starting player is: {players[next_first_player_idx]}")
        return rec_helper(players, moves, next_first_player_idx)
    else:
        index_of_player_to_remove = index_of_player_to_remove % num_players_left(players)
        print(f"From the following players that left: {players}")
        removed_player = players.pop(index_of_player_to_remove)
        print(f"We just removed the following player: {removed_player}")
        next_first_player_idx = index_of_player_to_remove % num_players_left(players) 
        print(f"New starting player is: {players[next_first_player_idx]}")
        return rec_helper(players, moves, next_first_player_idx)

        
s = Solution()

n = 5
k = 2


res = s.findTheWinner(n, k)
print(f"findTheWinner: {res}")
assert res == 3

# n = 6
# k = 5
# res = s.findTheWinner(n, k)
# print(f"findTheWinner: {res}")
# assert res == 1