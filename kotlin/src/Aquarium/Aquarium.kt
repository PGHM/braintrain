package Aquarium

class Aquarium (var length: Int = 20,
                var width: Int = 40,
                var height: Int = 50) {

    val volume : Int
        get() = width * height * length / 1000

    var waterCapacity = volume * 0.9

    constructor(numberOfFish: Int) : this(numberOfFish, numberOfFish / 2, numberOfFish / 3)
}