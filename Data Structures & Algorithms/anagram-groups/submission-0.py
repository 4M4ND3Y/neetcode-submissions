class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)

        for word in strs:
            count_char = [0 for _ in range(26)]

            for ch in word:
                i = ord(ch) - ord("a")
                count_char[i] += 1

            data[tuple(count_char)].append(word)

        return list(data.values())
