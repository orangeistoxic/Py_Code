def addText(text1, text2, sep = ' ', end = '.'):
    return text1 + sep + text2 + end
s = addText('Hi', 'James', '_', '?')
print(s)
s = addText('Hi', 'James')
print(s)
s = addText('Hi', 'James', '_')
print(s)
