# S is start. G is goal. 0 is moving. 1 is not moving.

import copy

def PrintRoute(route):
    dictionary = {'S':'S', 'G':'G', '0':'□', '1':'■', '2':'+'}
    for road in route:
        content = ''
        for element in road:
            content += dictionary[element]
        print(content)
    return

def Forward(route, moving, going):
    go = copy.deepcopy(going)
    go.append(moving)
    result = copy.deepcopy(route)
    result[moving[0]][moving[1]] = '2'
    return result, moving, go

def Available(route, position, going):
    # Maximum X-axis and Y-axis
    maxPosition = [len(route), len(route[0])]
    AvailableRoute = []
    goal = False
    for pos in range(0, len(position)):
        maxValue = maxPosition[pos]
        for i in [-1, 1]:
            if position[pos] + i < 0 or position[pos] + i >= maxValue:
                pass
            else:
                if pos == 0:
                    if route[position[0] + i][position[1]] == '0':
                        AvailableRoute.append([position[0] + i, position[1]])
                    elif route[position[0] + i][position[1]] == 'G':
                        goal = True
                else:
                    if route[position[0]][position[1] + i] == '0':
                        AvailableRoute.append([position[0], position[1] + i])
                    elif route[position[0]][position[1] + i] == 'G':
                        goal = True
    if AvailableRoute == []:
        if goal:
            print(' -- Route -- ')
            PrintRoute(route)
            print(going)
    return AvailableRoute

def SearchRoute(route, position, going=[]):
    # position is [ y-axis, x-axis ]
    # search route available for moving
    AvailableRoute = Available(route, position, going)
    for moving in AvailableRoute:
        road, location, go = Forward(route, moving, going)
        SearchRoute(road, location, go)
    return

def SearchStart(route):
    # search start position
    position = [] # y-axis, x-axis
    for road in range(0, len(route)):
        for element in range(0, len(route[road])):
            if route[road][element] == 'S':
                position = [road, element]
    return SearchRoute(route, position)

if __name__ == "__main__":
    # RouteMap = [
    #     ["0", 'S', '0', '0', '0'],
    #     ['0', '1', '1', '1', '0'],
    #     ['0', '0', '0', '0', '0'],
    #     ['0', '1', '0', '1', '1'],
    #     ['0', '1', '0', '0', 'G']
    # ]

    # RouteMap = [
    #     ["S", '0', '0', '0', '0'],
    #     ['1', '1', '1', '1', '0'],
    #     ['0', '0', '0', '0', '0'],
    #     ['0', '1', '1', '1', '0'],
    #     ['G', '1', '0', '0', '0']
    # ]

    RouteMap = []
    while True:
        try:
            road = input("")
            RouteMap.append(road.split(" "))
        except:
            print(" ")
            break

    print(' -- Road -- ')
    PrintRoute(RouteMap)
    SearchStart(RouteMap)
    
