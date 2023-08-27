class Rectangle:
    def __init__(self, Width, Length, Color):
        self.Width = Width
        self.Length = Length
        self.Color = Color
    def area(self):
        return self.Width * self.Length
    def perimeter(self):
        return (self.Width + self.Length) << 1
    def color(self):
        return self.Color[0].upper() + self.Color[1:].lower()

if __name__ == '__main__':
    arr = input().split()
    if int(arr[0]) > 0 and int(arr[1]) > 0:
        r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
    else:
        print("INVALID")