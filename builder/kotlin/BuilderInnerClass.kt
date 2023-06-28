fun main() {
    val builder = Pizza.Builder()
    builder.size("medium").crust("thick").ingredients("peperoni", "chesse").price(80.0)

    println(builder.build().toString())
}

class Pizza() {
    var size: String? = null
    var crust: String? = null
    var ingredients: List<String>? = null
    var price: Double? = null

    override fun toString() =
            """Pizza: 
            size = ${this.size}, 
            crust = ${this.crust}, 
            ingredients = ${this.ingredients}, 
            price = ${this.price}""".trimIndent()

    class Builder() {
        val pizza = Pizza()
        
        fun size(size: String): Builder {
            pizza.size = size
            return this
        }
        // La funcion de alcance apply() nos facilita la modificacion del objeto
        // y retonarlo con el nuevo estado modificado
        fun crust(crust: String) = apply { pizza.crust = crust }

        fun ingredients(vararg ingredients: String) = apply {
            pizza.ingredients = ingredients.toList()
        }

        fun price(price: Double) = apply { pizza.price = price }

        fun build() = pizza
    }
}
