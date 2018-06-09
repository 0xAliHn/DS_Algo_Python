def same_string(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


def is_substring(s, t):
    n = len(t)
    for i in range(0, len(s) - n + 1):
        if same_string(t, s[i:i+n]):
            return True
    return False


if __name__ == "__main__":
    # res = same_string("abcd","abcd")
    res = is_substring('sdfsfsabcdfdsfsf','abcd')
    print(res)
