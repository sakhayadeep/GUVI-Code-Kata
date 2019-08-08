def largest_palindrome(word):
    large = ""
    for i in range(len(word) - 1):
        for j in range(i + 1, len(word)+1):
            temp = word[i:j]
            if temp == temp[::-1] and len(temp) > len(large):
                large = temp
    return large


x = input()
print(len(x) - len(largest_palindrome(x)))
