import billboard


def billboardAPI():
    chart = billboard.ChartData('hot-100')

    list = []
    x = chart.__len__()
    current = 0
    new_data = []
    for current in range(100):
        raw_data = [(chart[current].artist + ' AND ' + chart[current].title)]
        for data in raw_data:
            new_data.append(str(data))
        current = current + 1
    return(new_data)

billboardAPI()
