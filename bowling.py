MAX_PINS = 10
MAX_FRAMES = 10


def is_strike(point: int) -> bool:
    return point == MAX_PINS


def is_spare(points: list) -> bool:
    return sum(points) == MAX_PINS


def get_total_score(point_list: list) -> int:
    total_score = 0
    point_index = 0

    for _ in range(MAX_FRAMES):
        if is_strike(point_list[point_index]):
            print("strike {} + {} + {}".format(MAX_PINS, point_list[point_index + 1], point_list[point_index + 2]))
            total_score += MAX_PINS + point_list[point_index + 1] + point_list[point_index + 2]
            point_index += 1
        elif is_spare(point_list[point_index:point_index + 2]):
            print("spare {} + {}".format(MAX_PINS, point_list[point_index + 2]))
            total_score += MAX_PINS + point_list[point_index + 2]
            point_index += 2
        else:
            print("{} + {}".format(point_list[point_index], point_list[point_index + 1]))
            total_score += point_list[point_index] + point_list[point_index + 1]
            point_index += 2
    print(total_score)
    return total_score
