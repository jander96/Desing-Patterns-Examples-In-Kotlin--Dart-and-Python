main() {
  final item = Circle(radius : 4);
  item.move(3, 3);
  item.draw();
  
  final item2 = Compose();
  item2.add(Dot());
  item2.add(Dot(x:4, y: 6));
  item2.add(Circle(x:5, y:5, radius:5));
  item2.move(5, 5);
  item2.draw();
}

abstract class Graphic {
  void move(int x, int y);
  void draw();
}

class Dot extends Graphic {
  Dot({this.x = 0, this.y = 0});
  int x;
  int y;

  void move(int x, int y) {
    x += x;
    y += y;
  }

  void draw() {
    print("Estoy dibujando un punto entre ${this.x} y ${this.y}");
  }
}

class Circle extends Graphic {
  Circle({this.x = 0, this.y = 0, this.radius = 0});
  int x;
  int y;
  int radius;

  void move(int x, int y) {
    x += x;
    y += y;
  }

  void draw() {
    print(
        "Estoy dibujando un circulo en ${this.x} y ${this.y} con radio  $radius");
  }
}

class Compose extends Graphic {
  final List<Graphic> _children = [];

  void move(int x, int y) {
    _children.forEach((child) => child.move(x, y));
  }

  void draw() {
    _children.forEach((child) => child.draw());
  }

  void add(Graphic child) => _children.add(child);

  void remove(Graphic child) => _children.remove(child);
}
