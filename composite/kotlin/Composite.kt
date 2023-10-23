fun main(){
    val item = Circle(radius = 4)
    item.move(3, 3)
    item.draw()

    val item2 = Compose()
    item2.add(Dot())
    item2.add(Dot(4,6))
    item2.add(Circle(5,5,5))
    item2.move(5, 5)
    item2.draw()

}

interface Graphic{
    fun move(x: Int,y : Int)
    fun draw()
}

class Dot(private var x: Int = 0, private var y : Int = 0): Graphic{

    override fun move(x: Int, y: Int) {
        this.x += x
        this.y += y
     }

    override fun draw() { 
        println("Estoy dibujando un punto entre ${this.x} y ${this.y}")
    }

}

class Circle(private var x: Int = 0, private var y : Int = 0, private var radius: Int = 0): Graphic{

    override fun move(x: Int, y: Int) {
        this.x += x
        this.y += y
     }

    override fun draw() { 
        println("Estoy dibujando un circulo en ${this.x} y ${this.y} con radio  $radius")
    }

}

class Compose(): Graphic{
    private val children: MutableList<Graphic> = mutableListOf()

    override fun move(x: Int, y: Int) {
        children.forEach{ it.move(x, y) }
     }

    override fun draw() {
        children.forEach{it.draw()}
     }

    fun add(child: Graphic) = children.add(child)

    fun remove(child: Graphic) = children.remove(child)
    
    

}