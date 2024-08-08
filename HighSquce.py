def highSquce(High_data):
    squce =[]
    max_flag = 0
    for values in High_data:
        if float(values[1]) > max_flag:
            squce.append('H')
            max_flag = float(values[1])
        else:
            squce.append('h')
            max_flag= float(values[1])

    return squce