def swingBottom(api_list):
    data =[]
    length = len(api_list)
    for i in range(2, length-2):
        if ((api_list[i][1] < api_list[i+1][1]) and (api_list[i][1] < api_list[i+2][1]) and (api_list[i][1] < api_list[i-1][1]) and (api_list[i][1] < api_list[i-2][1])):
            data.append(api_list[i])
            # print(api_list[i],api_list[i][1],"low+1: ",api_list[i+1][1]," low+2: ",api_list[i+2][1]," low-1: ",api_list[i-1][1]," low-2: ",api_list[i-2][1])
    return data