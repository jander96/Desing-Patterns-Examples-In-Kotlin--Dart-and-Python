interface Prototype<T>{
    fun  clone(): T
}

class File(private val content: String, val name: String) : Prototype<File>{
    fun showInfo(){
        println("Archivo ~~$name~~ tiene como contenido -> $content")
    }
    override fun clone() = this

}

fun main(){
    val file1 = File("Listado de precios topados para el 2024", "precios")
    val fileCopy = file1.clone()
    file1.showInfo()
    fileCopy.showInfo()
}