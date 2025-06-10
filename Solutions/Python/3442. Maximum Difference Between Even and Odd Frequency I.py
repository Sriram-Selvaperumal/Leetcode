class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1

        a = 0
        b = float('inf')
        for v in cnt:
            if v & 1:
                a = max(a, v)
            elif v:
                b = min(b, v)

        return a - (b if b != float('inf') else 0)
