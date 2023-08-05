


#  TC O(n) SC O(1)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1, n+1))
        print(f"New starting player is: {players[0]}")
        idx_player_to_remove = 0
        while len(players) > 1:
            idx_player_to_remove = (idx_player_to_remove + k - 1) % num_players_left(players)
            print(f"Removing player {players[idx_player_to_remove]}")
            players.pop(idx_player_to_remove)
            print(f"players left {players}")

        return players[0]
    

def num_players_left(players):
    return len(players)

        
s = Solution()

n = 5
k = 2


res = s.findTheWinner(n, k)
print(f"findTheWinner: {res}")
assert res == 3

n = 6
k = 5
res = s.findTheWinner(n, k)
print(f"findTheWinner: {res}")
assert res == 1