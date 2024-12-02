def isSolvable(words, result):
    mp = [-1] * (26)
    Hash = [0] * (26)
    CharAtfront = [0] * (26)
    uniq = ""
    
    for word in words:
        for i in range(len(word)):
            ch = word[i]
            Hash[ord(ch) - ord('A')] += pow(10, len(word) - i - 1)
            if mp[ord(ch) - ord('A')] == -1:
                mp[ord(ch) - ord('A')] = 0
                uniq += str(ch)
            if i == 0 and len(word) > 1:
                CharAtfront[ord(ch) - ord('A')] = 1
    
    for i in range(len(result)):
        ch = result[i]
        Hash[ord(ch) - ord('A')] -= pow(10, len(result) - i - 1)
        if mp[ord(ch) - ord('A')] == -1:
            mp[ord(ch) - ord('A')] = 0
            uniq += str(ch)
        if i == 0 and len(result) > 1:
            CharAtfront[ord(ch) - ord('A')] = 1
    
    mp = [-1] * (26)
    return solve(words, 0, 0, mp, [0] * 10, Hash, CharAtfront)


def solve(words, i, S, mp, used, Hash, CharAtfront):
    if i == len(words):
        return S == 0
    
    ch = words[i]
    for c in ch:
        val = mp[ord(c) - ord('A')]
        if val != -1:
            S += val * Hash[ord(c) - ord('A')]
        else:
            break
    else:
        return solve(words, i + 1, S, mp, used, Hash, CharAtfront)

    x = False
    for l in range(10):
        if CharAtfront[ord(ch[0]) - ord('A')] == 1 and l == 0:
            continue
        if used[l] == 1:
            continue
        mp[ord(ch[0]) - ord('A')] = l
        used[l] = 1
        x |= solve(words, i + 1, S + l * Hash[ord(ch[0]) - ord('A')], mp, used, Hash, CharAtfront)
        mp[ord(ch[0]) - ord('A')] = -1
        used[l] = 0
    
    return x


arr = ["SIX", "SEVEN", "SEVEN"]
S = "TWENTY"
if isSolvable(arr, S):
    print("YES")
else:
    print("NO")
