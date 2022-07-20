def is_isogram(string):
    string = string.upper()
    str = ""
    for s in string:
        if s == "" or s not in str:
            str+=s
    if str == string:
        print(True)
        return True
    else:
        print(False)
        return False

is_isogram("Dermatoglyphics"),
is_isogram(""),
is_isogram("isIsogram"),
is_isogram("moOse"),
is_isogram("aba"),
is_isogram("angst"),
is_isogram("flaVoR")