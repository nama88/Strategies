def lowSquce(Low_data):
    squce =[]
    min_flag = 0
    for values in Low_data:
        if float(values[1]) < min_flag:
            squce.append('l')
            min_flag = float(values[1])
        else:
            squce.append('L')
            min_flag= float(values[1])

    return squce