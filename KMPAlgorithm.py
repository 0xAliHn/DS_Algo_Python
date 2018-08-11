# Important References
# https://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
# https://www.youtube.com/watch?v=V5-7GzOfADQ


# O(n+m)
def build_prefix_table(pat):
    length = len(pat)
    pt = [0] * (length+1)

    for j in range(1, length):
        i = pt[j]

        while True:
            if pat[i] == pat[j]:
                pt[j+1] = pt[j]+1
                break

            else:
                pt[j+1] = 0
                break

    print(pt)
    return pt


def kmp(str, pat):
    n = len(str)
    m = len(pat)

    pt = build_prefix_table(pat)

    i, j = 0, 0

    while True:
        if i == n:
            return False
        if str[i] == pat[j]:
            i += 1
            j += 1
            if j == m:
                return True
        elif j == 0:
            i += 1
        else:
            j = pt[j]


print(kmp("ababcabcabababd", "ababd"))

