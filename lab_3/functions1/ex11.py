def palindrome(s):
    return s[::-1] == s

if __name__ == "__main__":
    s = input()
    print(palindrome(s))