# point = [x, y, z]
def calc_euclidean_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2) ** 0.5

def main():
    e_distance = calc_euclidean_distance([906,360,560], [466,668,158])
    print(e_distance)

main()