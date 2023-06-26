interface Silla{
    fun description(): String
}

interface Sofa{
    fun description(): String
}

interface Mesilla{
    fun description(): String
}


// Tenemos diferente variadades de estos productos Moderno y Victoriano 


//  Juego de estilo Victoriano
class SillaVictoriana : Silla{

    override fun description()= "silla victoriano"

}

class SofaVictoriano : Sofa{

    override fun description(): String = "sofa victoriano"

}

class MesillaVictoriana : Mesilla{

    override fun description(): String = "mesilla victoriano"

}


//Juego de estilo Moderno

class SillaModerna : Silla{

    override fun description()= "silla moderna"

}

class SofaModerno : Sofa{

    override fun description(): String = "sofa moderno"

}

class MesillaModerna : Mesilla{

    override fun description(): String = "mesilla moderna"

}

abstract class Factory {
    
    abstract fun crearSilla(): Silla

    abstract fun crearSofa(): Sofa

    abstract fun crearMesilla(): Mesilla


    fun combinarMuebles(): String =
        "Juego de muebles Silla: ${crearSilla().description()}\n Sofa: ${crearSofa().description()}\n Mesilla: ${crearMesilla().description()} "

}

class ModerFactory(): Factory(){

    override fun crearSilla(): Silla = SillaModerna()

    override fun crearSofa(): Sofa = SofaModerno()

    override fun crearMesilla(): Mesilla = MesillaModerna()

}

class VictorianFactory(): Factory(){

    override fun crearSilla(): Silla = SillaVictoriana()

    override fun crearSofa(): Sofa = SofaVictoriano()

    override fun crearMesilla(): Mesilla = MesillaVictoriana()

}

fun main(){
    entregarMuebles(ModerFactory())
    entregarMuebles(VictorianFactory())
}

fun entregarMuebles(factory: Factory){
    println(factory.combinarMuebles())
}