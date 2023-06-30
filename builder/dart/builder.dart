main() {
  // using builder with director class
  final carBuilder = CarBuilder();
  final director = Director(carBuilder);
  final deportiveBuilder = (director.getDeportiveCarBuilder() as CarBuilder).build();
  final truckBuilder = (director.getTruckBuilder() as CarBuilder).build();

  print(deportiveBuilder.toString());

  print(truckBuilder.toString());

  // using only builder

  final manualBuilder = ManualBuilder();

  final manual = (manualBuilder.setEngine("Deportive").makeDoors(2).setWheels(4)
          as ManualBuilder)
      .build();
  print(manual);
}

class Automovil {
  Automovil({this.engine = "Standar", this.doors = 4, this.wheel = 4});
  String engine;
  int doors;
  int wheel;

  @override
  String toString() {
    return "Automovil( engine = $engine, doors = $doors, whell = $wheel )";
  }
}

class Manual {
  final List<String> descriptions;

  Manual({required List<String> this.descriptions});

  @override
  String toString() {
    return "Manual( descriptions = $descriptions)";
  }
}

abstract class Builder {
  reset();
  Builder makeDoors(int doors);
  Builder setWheels(int wheel);
  Builder setEngine(String engine);
}

class CarBuilder extends Builder {
  Automovil car = Automovil();
  @override
  reset() {
    car = Automovil();
  }

  @override
  Builder makeDoors(int doors) {
    car.doors = doors;
    return this;
  }

  @override
  Builder setWheels(int wheel) {
    car.wheel = wheel;
    return this;
  }

  @override
  Builder setEngine(String engine) {
    car.engine = engine;
    return this;
  }

  Automovil build() {
    // Reset objet is optional when is build
    final automovil = car;
    reset();
    return automovil;
  }
}

class ManualBuilder extends Builder {
  Manual manual = Manual(descriptions: []);
  @override
  reset() {
    manual = Manual(descriptions: []);
  }

  @override
  Builder makeDoors(int doors) {
    manual.descriptions.add("Car has $doors doors");
    return this;
  }

  @override
  Builder setWheels(int wheel) {
    manual.descriptions.add("Car has $wheel wheels");
    return this;
  }

  @override
  Builder setEngine(String engine) {
    manual.descriptions.add("Car has $engine engines");
    return this;
  }

  Manual build() {
    return manual;
  }
}

class Director {
  final Builder builder;
  Director(this.builder);
  Builder getDeportiveCarBuilder() {
    return builder.setEngine("Deportive").makeDoors(2).setWheels(4);
  }

  Builder getTruckBuilder() {
    return builder.setEngine("big").makeDoors(2).setWheels(8);
  }
}
