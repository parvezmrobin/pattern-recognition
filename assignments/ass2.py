from math import inf
from queue import PriorityQueue

true, false, null = True, False, None


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def draw(self):
        pass

    def draw_to(self):
        pass

    def slope_to(self, other):
        del_y = other.y - self.y
        del_x = other.x - self.x
        if del_x == 0:
            if del_y == 0:
                return -inf
            return inf
        return del_y / del_x

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        return self.slope_to(Point.CENTER) == other.slope_to(Point.CENTER)

    def __ne__(self, other):
        return self.slope_to(Point.CENTER) != other.slope_to(Point.CENTER)

    def __le__(self, other):
        return self.slope_to(Point.CENTER) <= other.slope_to(Point.CENTER)

    def __lt__(self, other):
        return self.slope_to(Point.CENTER) < other.slope_to(Point.CENTER)

    def __ge__(self, other):
        return self.slope_to(Point.CENTER) >= other.slope_to(Point.CENTER)

    def __gt__(self, other):
        return self.slope_to(Point.CENTER) > other.slope_to(Point.CENTER)


Point.CENTER = Point(0, 0)


def get_lines_by_sorting(points):
    # Ensure call by value
    points = points[:]  # type: list
    lines = []

    for cling in points:
        queue = PriorityQueue()

        for point in points:
            queue.put((point.slope_to(cling), point))

        current_slop, line = null, []
        while not queue.empty():
            slop, point = queue.get()
            if slop == current_slop:
                line.append(point)
            else:
                if len(line) > 2:
                    lines.append([cling] + line)
                line = [point]
                current_slop = slop

    return lines


def is_line(line):

    p0, p1, p2, p3 = line  # type: Point
    if p0.slope_to(p1) == p0.slope_to(p2) == p0.slope_to(p3):
        return true
    return false


def get_lines_by_backtracking(points):
    # Ensure call by value
    points = points[:]  # type: list
    lines = []

    for p0 in points:
        for p1 in points:
            if p0.slope_to(p1) != -inf:
                for p2 in points:
                    if p0.slope_to(p2) != -inf and p1.slope_to(p2) != -inf:
                        for p3 in points:
                            if p0.slope_to(p3) != -inf and p1.slope_to(p3) != -inf and p2.slope_to(p3) != -inf:
                                line = [p0, p1, p2, p3]
                                if is_line(line):
                                    lines.append(line)
    return lines


def remove_subsets(lines):
    length = len(lines)
    lines = [sorted(line) for line in lines]
    mask = [true] * length

    for i in range(length):
        if mask[i]:
            for j in range(i + 1, length):
                if lines[i][-4:] == lines[j][-4:]:
                    mask[j] = false
    new_list = [lines[i] for i, m in enumerate(mask) if m]
    return new_list


def main():
    points = [(19000, 10000), (18000, 10000), (32000, 10000), (21000, 10000), (1234, 5678), (14000, 10000), ]
    # points = [(10000, 0), (0, 10000), (3000, 7000), (7000, 3000), (20000, 21000), (3000, 4000), (14000, 15000),
    #           (6000, 7000), ]
    points = [Point(*point) for point in points]
    lines = get_lines_by_backtracking(points)
    lines = remove_subsets(lines)
    for line in lines:
        print(*line, sep=' -> ')


main()
