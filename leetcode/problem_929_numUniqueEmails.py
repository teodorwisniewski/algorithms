from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            idx, local = 0, ''
            while email[idx] not in ['@', '+']:
                if email[idx] != '.':
                    local += email[idx]
                idx += 1
            
            while email[idx] != '@':
                idx += 1
            
            domain = email[idx+1:]
            unique.add((local, domain))

        return len(unique)
        



sol = Solution()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
res = sol.numUniqueEmails(emails)
print(f"numUniqueEmails {res}")