def convert_to_map(points_list):
    h = {}
    for point in points_list:
        h[point[0]] = int(point[1])

    return h

def max_score_path(travel_time,points, path, curr,  tot_score, tot_cost, maximum, max_path_so_far):
    if "END" in curr:
        if tot_score-tot_cost > maximum:
            maximum = tot_score-tot_cost
            max_path_so_far = path
            # return somehow
    for node in travel_time:
        if curr == node[0]:
            max_score_path(travel_time, points, path+=curr, node[1], tot_score+points[node[1]] , tot_cost+int(node[2]), maximum , max_path_so_far)

    return (maximum,max_path_so_far)

points = convert_to_map(points_list)
print (max_score_path(travel_time, points, [], "START", 0, 0, -1000,[]))
