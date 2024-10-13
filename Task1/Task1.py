def is_palindrome(s):
    # 将字符串统一为小写并移除非字母数字字符
    clean_s = ''.join(c for c in s.lower() if c.isalnum())
    # 检查处理后的字符串是否为回文
    return clean_s == clean_s[::-1]

test_string = "A man, a plan, a canal: Panama"
print(is_palindrome(test_string)) 