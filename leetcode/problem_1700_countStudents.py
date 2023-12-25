from typing import List
from collections import deque, Counter
import pdb


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:     
        students_cnt = Counter(students)
        queue = deque(students)
        sandwiches_stack = deque(sandwiches)
        
        while sandwiches_stack and students_cnt[sandwiches_stack[0]] > 0:
            if sandwiches_stack[0] == queue[0]:
                students_cnt[sandwiches_stack.popleft()] -= 1
                queue.popleft()
            else:
                first_person_in_queue = queue.popleft()
                queue.append(first_person_in_queue)

        return len(queue)

