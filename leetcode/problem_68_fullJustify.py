from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res = []
        line, line_len = [], 0
        idx = 0

        while idx < len(words):
            if (line_len + len(line) + len(words[idx])) > maxWidth:
                extra_space = maxWidth - line_len
                spaces = extra_space // max(1, len(line) - 1)
                remainder = extra_space % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                res.append("".join(line))
                line, line_len = [], 0
            
            line.append(words[idx])
            line_len += len(words[idx])
            idx += 1

        # handling last line - left justified
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        res.append(last_line + " " * trail_space)
        
        return res


        




sol = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
res = sol.fullJustify(words, maxWidth)
print(f"fullJustify {res}")

expected_res = [
   "This    is    an",
   "example  of text",
   "justification.  "
]

assert res == expected_res