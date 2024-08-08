def swingTop(api_list):
    data=[]
    length = len(api_list)
# n = int(inpucollectiont())  this will be used for specifying the counter for swing top
    for i in range(2,length-2):
        if ((api_list[i][1] > api_list[i+1][1]) and (api_list[i][1] > api_list[i+2][1]) and (api_list[i][1] > api_list[i-1][1]) and (api_list[i][1] > api_list[i-2][1])):
            data.append(api_list[i])

    return data