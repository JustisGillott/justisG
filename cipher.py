m_unicode = ord("M")
text = "i am in class"
shift = 3
var = ""
for m in text:
    m = m.upper()
    if m == " ":
        print(" ")
    else:
        print(chr(ord(m) + shift))
        var += m