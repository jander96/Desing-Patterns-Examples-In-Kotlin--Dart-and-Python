class Singleton private constructor() {
    companion object {
        private var instance: Singleton? = null

        fun instance(): Singleton {
            if (instance == null) {
                instance = Singleton()
            }
            return instance!!
        }
    }
}

object SingletonByObjet{ }

fun main() {
    val instance1 = Singleton.instance()
    val instance2 = Singleton.instance()
    val instance3 = Singleton.instance()
    val instance4 = Singleton.instance()

    val object1 = SingletonByObjet
    val object2 = SingletonByObjet
    val object3 = SingletonByObjet
    val object4 = SingletonByObjet

    println(instance1)
    println(instance2)
    println(instance3)
    println(instance4)
    println("--------------------------")
    println(object1)
    println(object2)
    println(object3)
    println(object4)
}
