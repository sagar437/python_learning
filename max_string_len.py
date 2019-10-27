def max_len_string(str):
    max_len = 0
    dict = {}
    for i in str:
        if i not in dict:
            dict[i] = 1
        else:
            if len(dict) > max_len:
                max_len = len(dict)
            else:
                pass
	dict = {}
	print(dict)
    print(max_len)
max_len_string("pwwkew")
