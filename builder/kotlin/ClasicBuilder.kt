fun main() {
    // using builder with director class
    val carBuilder = CarBuilder()
    val director = Director(carBuilder)
    val deportiveBuilder = director.getDeportiveCarBuilder() as CarBuilder
    val truckBuilder = director.getTruckBuilder() as CarBuilder

    println(deportiveBuilder.build().toString())

    println(truckBuilder.build().toString())

    // using only builder

    val manualBuilder = ManualBuilder()

    val manual =
            (manualBuilder.setEngine("Deportive").makeDoors(2).setWheels(4) as ManualBuilder)
                    .build()
    println(manual)
}

data class Automovil(var engine: String = "Standar", var doors: Int = 4, var wheel: Int = 4)

data class Manual(val descriptions: MutableList<String> = mutableListOf())

interface Builder {
    fun reset()
    fun makeDoors(doors: Int): Builder
    fun setWheels(wheel: Int): Builder
    fun setEngine(engine: String): Builder
}

class CarBuilder() : Builder {
    var car: Automovil = Automovil()
    override fun reset() {
        car = Automovil()
    }

    override fun makeDoors(doors: Int): Builder {
        car.doors = doors
        return this
    }

    override fun setWheels(wheel: Int): Builder {
        car.wheel = wheel
        return this
    }

    override fun setEngine(engine: String): Builder {
        car.engine = engine
        return this
    }

    fun build(): Automovil {
        // Reset objet is optional when is build
        val automovil = car
        reset()
        return automovil
    }
}

class ManualBuilder() : Builder {
    var manual: Manual = Manual()
    override fun reset() {
        manual = Manual()
    }

    override fun makeDoors(doors: Int): Builder {
        manual.descriptions.add("Car has $doors doors")
        return this
    }

    override fun setWheels(wheel: Int): Builder {
        manual.descriptions.add("Car has $wheel wheel")
        return this
    }

    override fun setEngine(engine: String): Builder {
        manual.descriptions.add("Car engine is type $engine")
        return this
    }
    // here is not reseted the object
    fun build(): Manual = manual
}

class Director(private val builder: Builder) {

    fun getDeportiveCarBuilder(): Builder {

        return builder.setEngine("Deportive").makeDoors(2).setWheels(4)
    }

    fun getTruckBuilder(): Builder {
        return builder.setEngine("big").makeDoors(2).setWheels(8)
    }
}
