import collections
from typing import List


# 트라이 저장용 노드.
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 펠린드롬 판별 함수.
    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    # 단어 삽입.
    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            # 두번째 로직에서 문자를 하나씩 제거해가며 팰린드롬을 판별해서 체크함.
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root

        # 여기 while 에서 node = nod.children[word[0]]으로 node 끝까지 타고 가서 밑에 판별 로직 1, 2에서 끝점이랑 비교가 가능해짐.
        while word:
            # 판별 로직 3
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        """
        판별 로직 1 
        위쪽 while 문에서 구현된 트라이와 word가 맞을 때 까지 쭉 안으로 들어오고 그 지점에서 if 문이 실행됨.
        즉, 꺼꾸로 들어간 트라이와 원래의 word 값이 같은 경우에 밑의 if문으로 걸러짐. 
        """
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        """
        판별 로직 2
        위쪽 while 문에서 구현된 트라이와 word가 맞을 때 까지 쭉 안으로 들어오고 그 지점에서 if 문이 실행됨.
        그 자리에 palindrome_word_id가 있으면 그것도 정답. 
        """
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results


a = Solution().palindromePairs(['d', 'cbbcd', 'dcbb', 'dcbc', 'cbbc', 'bbcd'])
print(a)
