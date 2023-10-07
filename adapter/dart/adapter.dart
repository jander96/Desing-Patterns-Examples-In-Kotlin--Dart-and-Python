main() {
  final specialLibrary = SpecialLibrary();
  final adapter = Adapter(specialLibrary);

  print(adapter.getData());
}

class SpecialLibrary {
  String getData() => "atad litu";
}

abstract class Data {
  String getData();
}

class Adapter implements Data {
  final SpecialLibrary library;

  Adapter(this.library);

  String getData() {
    final rawData = library.getData();
    return rawData.splitMapJoin(RegExp('i'),
        onMatch: (m) => '${m[0]}', onNonMatch: (n) => '*');
  }
}
