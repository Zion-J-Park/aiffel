
strTest = 'Hello World! ISE'
print(strTest[5:len(strTest):-1])

str = ['h','e','l','l','o']
# str = ['h','a','n','n','a','h']
print(str)

# def reverseStr(str):
#     str = str[::-1]
#     print(str)

# def reverseStr(str):
#     str.reverse()
#     print(str)
str.reverse()
# print()
print(str)

# reverseStr(str)

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
logs.sort()
print(logs)
digs = logs[:2]
print(digs)
lets = logs[2:3]
lets = lets + logs[:-3:-1]
print(lets)
logs = lets + digs
print(logs)

# logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
# logs.sort()
# print(logs)