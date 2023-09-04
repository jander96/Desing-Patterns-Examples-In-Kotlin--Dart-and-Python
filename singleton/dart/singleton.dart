class Singleton {
  Singleton._();
  factory Singleton() => _singleton;
  static final Singleton _singleton = Singleton._();

  @override
  String toString() => '${this.hashCode}';
}

main() {
  final instance1 = Singleton();
  final instance2 = Singleton();
  final instance3 = Singleton();
  final instance4 = Singleton();

  print(instance1);
  print(instance2);
  print(instance3);
  print(instance4);
}
