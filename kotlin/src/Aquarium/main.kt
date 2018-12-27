package Aquarium

fun main(args: Array<String>) {
    val myAquarium = Aquarium(50, 40, 30)
    println(myAquarium.volume)
    val mySecondAquarium = Aquarium(50)
    println(mySecondAquarium.volume)
}