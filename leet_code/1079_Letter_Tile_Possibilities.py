
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        results = []
        MAX_NUM = len(tiles) 

        def backtrack(seq, tiles):

            if len(seq) > MAX_NUM:
                return 

            if len(seq) > 0 and seq not in results:
                results.append(seq)
            
            for i in range(len(tiles)):
                new_letter = tiles.pop(0)
                backtrack(seq+new_letter, tiles)
                tiles.append(new_letter)

        backtrack("", list(tiles))
        return len(results)
            

s = Solution()

res = s.numTilePossibilities("AAB")
print(f"numTilePossibilities {res}")