abstract class Prototype<T> {
  T clone();
}

class File extends Prototype<File> {
  final String name;
  final String _content;

  File(this.name, this._content);

  @override
  File clone() => this;

  void showInfo() {
    print("Archivo ~~$name~~ tiene como contenido -> $_content");
  }
}

void main() {
  final file1 = File('precios', 'Listado de precios para el 2024');
  final fileCopy = file1.clone();

  file1.showInfo();
  fileCopy.showInfo();
}
