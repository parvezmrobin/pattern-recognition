"""
Problem statement can be found in *Pattern Recognition Assignment 2.pdf*
in the same folder.
"""

from math import inf
from queue import PriorityQueue

from matplotlib.pyplot import plot, show, text

true, false, null = True, False, None


class Point:
    def __init__(self, x, y):
        self.x, self.y = int(x), int(y)

    def draw(self, color='b', show_text=false, offset=(0, 0)):
        plot(self.x, self.y, color + 'o')
        if show_text:
            text(self.x + offset[0], self.y + offset[1], self, fontsize=6)

    def draw_to(self, other, color='r'):
        plot([self.x, other.x], [self.y, other.y], color + '-')

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

    def __del__(self):
        show()


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
                line = [cling] + line
                if len(line) > 2 and sorted(line) == line:
                    lines.append(line)
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
                                    sorted_line = sorted(line)
                                    if sorted_line == line:
                                        lines.append(sorted_line)
                                        # print(sorted_line)
    return lines


def main():
    with open('../input/assignment2/input3.txt') as file:
        n = int(file.readline())
        points = []
        for i in range(n):
            x, y = file.readline().split()
            points.append(Point(x, y))

    lines = get_lines_by_sorting(points)

    for point in points:
        point.draw(show_text=true, offset=(100, -500))

    for line in lines:
        for i, point in enumerate(line):
            if i > 0:
                point.draw_to(line[i - 1])
        print(*line, sep=' -> ')
    show()


main()
