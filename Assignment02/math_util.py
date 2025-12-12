import math
def calculate_circle_area(rad):
    """calculate the area of the circle given its radius"""
    if rad < 0:
        raise ValueError("eadius cannot be negative")
    area_circle = math.pi * rad ** 2
    return area_circle

def calculate_rectangle_area(length,width):
    """calculate the area of the rectangle given its length and width"""
    if length < 0 or width <0:
        raise ValueError("lenth and width cannot be negative")
    area_rectangle = length *width
    return area_rectangle

if __name__ =="__main__":
    rad = int(input("Enter the radius of the circle:"))
    circle = calculate_circle_area(rad)
    print(f" area for the radius: {rad} is {circle}")

    len = int(input("Enter the length of the rectacngle : "))
    wid = int(input("Enter the width of the rectangle : "))
    rectangle = calculate_rectangle_area(len,wid)
    print(f"area for the rectangle with length {len} and width {wid} is {rectangle}")

