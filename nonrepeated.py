def first_non_repeated(string):
   char_count = {}
   for char in string:
     if char not in char_count:
       char_count[char] = 1
     else:
       char_count[char] += 1
   for char in string:
     if char_count[char] == 1:
       return char
   return None
print(first_non_repeated("abcdeffghijklmnopqrstuvwxyz"))
print(first_non_repeated("aabbccddeeffgg"))
print(first_non_repeated("abcdefg"))
