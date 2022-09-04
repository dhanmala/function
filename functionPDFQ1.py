def my_function(words):
  ctr = 0
  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr
print(my_function(['abc', 'xyz', 'aba', '1221']))
