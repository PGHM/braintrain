import java.util.*

fun main(args: Array<String>) {
    println("Hello ${args[0]}!")
    feedTheFish()

    val foo = {foo: (String, Int, Int) -> Boolean -> foo("Sunday", 1, 1)}
    println(foo(::shouldChangeWater))
}

fun feedTheFish() {
    val day = randomDay()
    val food = foodForDay(day)
    println("Today is $day and the fish eat $food")

    if (shouldChangeWater(day)) {
        println("Should change the water!")
    } else {
        println("Yay free day, no need to change water")
    }
}

fun shouldChangeWater(day: String, temperature: Int = 22, dirty: Int = 20) : Boolean {
    return when {
        temperature > 30 -> true
        dirty > 30 -> true
        day == "Sunday" -> true
        else -> false
    }
}

fun randomDay() : String {
    val week = listOf("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    return week[Random().nextInt(week.size)]
}

fun foodForDay(day : String) : String {
    return when (day) {
        "Monday" -> "flakes"
        "Tuesday" -> "pellets"
        "Wednesday" -> "redworms"
        "Thursday" -> "granules"
        "Friday" -> "mosquitos"
        "Saturday" -> "lettuce"
        "Sunday" -> "plankton"
        else -> "defaultFood"
    }
}