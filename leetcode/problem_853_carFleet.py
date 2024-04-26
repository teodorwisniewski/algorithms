from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos_speed = [(pos, speed) for pos, speed in zip(position, speed)]

        stack = []
        for pos, speed in sorted(pos_speed, reverse=True):
            distance_to_traverse = target - pos
            time_to_reach_target = distance_to_traverse / speed
            stack.append(time_to_reach_target)
            print(f"adding time_to_reach_target to the stack {time_to_reach_target} stack: {stack}")
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                print(f"popping time_to_reach_target from the stack {time_to_reach_target}, it was slow down by {stack[-2]}")
                stack.pop()
            

        return len(stack)
       




if __name__ == "__main__":

    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    expected_output = 3
    sol = Solution()
    output = sol.carFleet(target, position, speed)
    print(f"sol.carFleet(target, position. speed) {output}")
    assert output == expected_output
        