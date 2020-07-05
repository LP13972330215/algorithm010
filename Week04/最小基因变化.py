class Solution:
    def minMutation(self, start, end, bank):

        queue, count, bankset = [(start, 0)], 0, set(bank)
        while queue:
            cur, step = queue.pop(0)
            if cur == end:
                return step
            for i in range(len(cur)):
                for c in "ACGT":
                    new = cur[:i]+ c + cur[i+1:]
                    if new in bankset:
                        bankset.remove(new)
                        queue.append((new, step+1))
        return -1

if __name__ == '__main__':
    start="AACCGGTT"
    end="AAACGGTA"
    bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print(Solution().minMutation(start,end,bank))
