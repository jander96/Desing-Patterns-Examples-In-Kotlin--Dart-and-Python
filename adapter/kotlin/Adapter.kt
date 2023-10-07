fun main(){
    val specialLibrary = SpecialLibrary()
    val adapter = Adapter(specialLibrary)

    print(adapter.getData())

}

class SpecialLibrary(){
    fun getData(): String = "atad litu"
}

interface Data{
    fun getData(): String
}


class Adapter(private val library: SpecialLibrary) : Data{

    override fun getData(): String{
        val rawData = library.getData()
        return rawData.reversed()
    }

}