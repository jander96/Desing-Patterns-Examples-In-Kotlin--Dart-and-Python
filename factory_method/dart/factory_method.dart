import 'product_interface.dart';

main() {
  final carTransportation = CarDeliveryTransportFactory();
  final bikeTrasportation = BikeDeliveryTransportFactory();

  carTransportation.transportOrder();
  bikeTrasportation.transportOrder();

  carTransportation.reparingVehicle();
  bikeTrasportation.reparingVehicle();
}

abstract class TransportDeliveryFactory {
  abstract final Vehicle vehicle;

  transportOrder() {
    print("the order is moving in $vehicle ");
  }

  reparingVehicle() {
    print("the $vehicle is in garage ");
  }

  Vehicle createVehicle();
}

class Car extends Vehicle {
  @override
  start() {
    print("start engine");
  }

  @override
  stop() {
    print("stop engine");
  }
}

class Bike extends Vehicle {
  @override
  start() {
    print("start pedal");
  }

  @override
  stop() {
    print("stop pedal");
  }
}

class CarDeliveryTransportFactory extends TransportDeliveryFactory {
  @override
  Vehicle createVehicle() => Car();

  @override
  Vehicle get vehicle => createVehicle();
}
class BikeDeliveryTransportFactory extends TransportDeliveryFactory {
  @override
  Vehicle createVehicle() => Bike();

  @override
  Vehicle get vehicle => createVehicle();
}

