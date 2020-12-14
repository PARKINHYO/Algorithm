from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letters, digits = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        print(letters)
        letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))

        print(letters)

        return letters + digits
