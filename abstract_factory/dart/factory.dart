abstract class Silla {
  String description();
}

abstract class Sofa {
  String description();
}

abstract class Mesilla {
  String description();
}

// Tenemos diferente variadades de estos productos Moderno y Victoriano

//  Juego de estilo Victoriano
class SillaVictoriana extends Silla {
  @override
  String description() => 'silla victoriana';
}

class SofaVictoriano extends Sofa {
  @override
  String description() => 'sofa victoriano';
}

class MesillaVictoriana extends Mesilla {
  @override
  String description() => 'mesilla victoriano';
}

//Juego de estilo Moderno

class SillaModerna extends Silla {
  @override
  String description() => 'silla Moderna';
}

class SofaModerno extends Sofa {
  @override
  String description() => "sofa moderno";
}

class MesillaModerna extends Mesilla {
  @override
  String description() => "mesilla moderno";
}

abstract class Factory {
  Silla crearSilla();

  Sofa crearSofa();

  Mesilla crearMesilla();

  String combinarMuebles() =>
      "Juego de muebles Silla: ${crearSilla().description()}\n Sofa: ${crearSofa().description()}\n Mesilla: ${crearMesilla().description()} ";
}

class ModerFactory extends Factory {
  @override
  Mesilla crearMesilla() => MesillaModerna();

  @override
  Silla crearSilla() => SillaModerna();

  @override
  Sofa crearSofa() => SofaModerno();
}

class VictorianFactory extends Factory {
  @override
  Mesilla crearMesilla() => MesillaVictoriana();

  @override
  Silla crearSilla() => SillaVictoriana();

  @override
  Sofa crearSofa() => SofaVictoriano();
}

main() {
  entregarMuebles(ModerFactory());
  entregarMuebles(VictorianFactory());
}

entregarMuebles(Factory fact) {
  print(fact.combinarMuebles());
}
