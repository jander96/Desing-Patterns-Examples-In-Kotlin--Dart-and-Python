

fun main(){
    val carTransportation = CarDeliveryTransportFactory()
    val bikeTrasportation = BikeDeliveryTransportFactory()

    carTransportation.transportOrder()
    bikeTrasportation.transportOrder()

    carTransportation.reparingVehicle()
    bikeTrasportation.reparingVehicle()
}



abstract class TransportDeliveryFactory{
    abstract val vehicle : Vehicle

    fun transportOrder(){
        println("the order is moving in $vehicle ")
    }
    fun reparingVehicle(){
        println("the $vehicle is in garage ")
    }

    abstract fun createVehicle():Vehicle
}

interface Vehicle {
    fun start()
    fun stop()
}

class Car() : Vehicle{

    override fun start() {
        println("start engine")

     }

    override fun stop() {
        println("stop engine")
     }
     override fun toString() = "Car"
}

class Bike(): Vehicle{

    override fun start() { 
        println("start pedal")
    }

    override fun stop() {
        println("stop pedal")
     }
     override fun toString() = "Bike"
}


class CarDeliveryTransportFactory() : TransportDeliveryFactory(){

    override val vehicle: Vehicle = createVehicle()

    override fun createVehicle(): Vehicle { 
        return Car()
    }

}

class BikeDeliveryTransportFactory(): TransportDeliveryFactory(){

    override val vehicle: Vehicle = createVehicle()

    override fun createVehicle(): Vehicle = Bike()

}