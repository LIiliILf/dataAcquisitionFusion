# re.search() 从左到右扫描字符串，尝试匹配正则表达式，一旦找到第一个匹配结果就返回match，如果没有找到匹配结果就返回None。



import re
# 1、字符"\d"匹配0-9之间的一个数值。
reg1 = r"\d"
m1 = re.search(reg1, "abc123cd")
print("re1")
print('abc123cd用\d匹配第一个数字，结果为1',m1)
# 结果找到了第一个数值1

# 2、字符"+"重复前面一个匹配字符一次或者多次。
reg2 = r"b\d+"
m2 = re.search(reg2, "a12b123c")
print("re2")
print(m2)

# 3、字符"*"重复前面一个匹配字符0次或者多次。
reg3_1 = r"ab+"
m3_1 = re.search(reg3_1, "acabc")
print("re3")
print(m3_1)
reg3_2 = r"ab*"
m3_2 = re.search(reg3_2, "acabc")
print(m3_2)
print("--------------------------")

# 4.字符"?"重复前面一个匹配字符零次或者一次。
reg4 = r"ab?"
m4 = re.search(reg4, "abbcabc")
print("re4")
print(m4)
# 结果为“ab”说明“ab?”匹配到了1次b。
print("--------------------------")

# 5.字符"."代表任何一个字符，但是没有特别声明时不代表字符"\n"。
s = "xaxby"
m5 = re.search(r"a.b", s)
print("re5")
print(m5)
# 结果为“axb”说明“a.b”匹配到了“axb”。
print("--------------------------")

# 6 "|"代表把左右分成两个部分。
s = "xaabababy"
m6 = re.search(r"ab|ba", s)
print("re6")
print(m6)
# 结果为“ab”说明“ab”在前面，所以匹配到了“ab”。
print("--------------------------")

# 7 特殊字符使用反斜线"\"引导，例如"\r"、"\n"、"\t"、"\\"分别表示回车、换行、制表符号与反斜线自己本身。
reg7 = r"a\nb?"
m7 = re.search(reg7, "ca\nbcabc")
print("re7")
print(m7)
# 结果为 “a\nb” 说明"\n"没有被转义。
print("--------------------------")

# 8 字符“\b”来匹配单词边界，它本身不匹配任何字符。
# 匹配单词（由字母数字或下划线组成的）的开始或结束(匹配开始时，单词之前不能有\w;
# 匹配结束时，单词之后不能有\w)。
reg8 = r"car\b"
m8 = re.search(reg8, "car ")
print("re8")
print(m8)
# 结果为“car”因为“car”后面是空格。
print("--------------------------")

# 9 "[]"中的字符是任选择一个，如果字符是ASCII码中连续的一组，那么可以使用"-"符号连接，
# 例如[0-9]表示0-9的其中一个数字，[A-Z]表示A-Z的其中一个大写字符，[0-9A-Z]表示0-9的其中一个数字或者是A-Z的其中一个大写字符。
reg9 = r"x[0-9]y"
m9 = re.search(reg9, "xyx2y")
print("re9")
print(m9)
# 结果为“x2y”说明“x[0-9]y”匹配到了“x2y”。
print("--------------------------")

# 10 "^"出现在[]的第一个字符位置，就代表取反，例如[^ab0-9]表示不是a、b，也不是0-9的数字。
reg10 = r"x[^ab0-9]y"
m10 = re.search(reg10, "xayx2yxcy")
print("re10")
print(m10)
# 结果为“xcy”说明“x[^ab0-9]y”匹配到了“xcy”。
print("--------------------------")

# 11 "\s"匹配任何空白字符，等价"[\r\n\x20\t\f\v]"。
s = "1a ba\tbxy"
m11 = re.search(r"a\sb", s)
print("re11")
print(m11)
# 结果为“a b”说明“a\sb”匹配到了“a b”。
print("--------------------------")

# 12 "\w"匹配包括下划线子内的单词字符，等价于"[a-zA-Z0-9_]"。
reg12 = r"\w+"
m12 = re.search(reg12, "Python is easy")
print("re12")
print(m12)
# 结果为“Python”说明“\w+”匹配到了“Python”。
print("--------------------------")

# 13 "^"匹配字符串的开头位置。
reg13 = r"^ab"
m13 = re.search(reg13, "cabcab")
print("re13")
print(m13)
# 结果为“None”说明“^ab”没有匹配到“cabcab”。
print("--------------------------")

# 14 "$"匹配字符串的结尾位置。
reg14 = r"ab$"
m14 = re.search(reg14, "abcab")
print("re14")
print(m14)
# 结果是最后一个“ab”
print("--------------------------")

# 15 使用括号(...)可以把(...)看成一个整体，经常与"+"、"*"、"?"的连续使用，对(...)部分进行重复。
reg15=r"(ab)+"
m15=re.search(reg15,"ababcab")
print("re15")
print(m15)
#结果匹配"abab"，"+"对"ab"进行了重复：
#<_sre.SRE_Match object; span=(0, 4), match='abab'>
