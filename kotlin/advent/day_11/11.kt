import java.io.File
import ElementType.*
import com.sun.javaws.exceptions.InvalidArgumentException
import java.io.InvalidClassException

enum class ElementType {
    POLONIUM,
    THULIUM,
    PROMETHIUM,
    RUTHENIUM,
    COBALT
}

data class Floor(
    val chips: MutableList<ElementType> = mutableListOf(),
    val generators: MutableList<ElementType> = mutableListOf()
) {
    var isEmpty = chips.isEmpty() && generators.isEmpty()
}

fun main() {
    val floors = listOf(
        Floor(
            mutableListOf(THULIUM, RUTHENIUM, COBALT),
            mutableListOf(THULIUM, RUTHENIUM, COBALT, PROMETHIUM, POLONIUM)
        ),
        Floor(chips = mutableListOf(POLONIUM, PROMETHIUM)),
        Floor(),
        Floor()
    )

    println("Steps required to move everything to floor 4 was ${moveChipsOrGenerators(floors, 0, 0)}")
}

tailrec fun moveChipsOrGenerators(floors: List<Floor>, elevatorFloorIndex: Int, stepsTaken: Int): Int {
    println("Floors")
    println(floors)
    if (floors[0].isEmpty && floors[1].isEmpty && floors[2].isEmpty) return stepsTaken

    if (tryToMoveElevatorDown(elevatorFloorIndex, floors)) {
        return moveChipsOrGenerators(floors, elevatorFloorIndex - 1, stepsTaken + 1)
    }

    moveElevatorUp(elevatorFloorIndex, floors)
    return moveChipsOrGenerators(floors, elevatorFloorIndex + 1, stepsTaken + 1)
}

fun moveElevatorUp(elevatorFloorIndex: Int, floors: List<Floor>) {
    val elevatorFloor = floors[elevatorFloorIndex]
    val upperFloor = floors[elevatorFloorIndex + 1]

    if (elevatorFloor.chips.size == 1 && elevatorFloor.generators.size == 1) {
        upperFloor.generators.add(elevatorFloor.generators.removeFirst())
        upperFloor.chips.add(elevatorFloor.chips.removeFirst())
        return
    }

    if (elevatorFloor.generators.size >= 2 && upperFloor.generators.isNotEmpty()) {
        upperFloor.generators.add(elevatorFloor.generators.removeFirst())
        upperFloor.generators.add(elevatorFloor.generators.removeFirst())
    }

    if (elevatorFloor.chips.size >= 2 && upperFloor.generators.isEmpty()) {
        upperFloor.chips.add(elevatorFloor.chips.removeFirst())
        upperFloor.chips.add(elevatorFloor.chips.removeFirst())
        return
    }

    //TODO: you end here you dummy!
}

fun tryToMoveElevatorDown(elevatorFloorIndex: Int, floors: List<Floor>): Boolean {
    if (elevatorFloorIndex == 0) return false

    val elevatorFloor = floors[elevatorFloorIndex]
    val lowerFloor = floors[elevatorFloorIndex - 1]

    if (lowerFloor.isEmpty) return false

    if (elevatorFloor.chips.isNotEmpty() && lowerFloor.generators.isEmpty()) {
        lowerFloor.chips.add(elevatorFloor.chips.removeFirst())
        return true
    }

    elevatorFloor.generators.intersect(lowerFloor.chips).firstOrNull()?.let {
        elevatorFloor.generators.remove(it)
        lowerFloor.generators.add(it)
        return true
    }

    elevatorFloor.chips.intersect(lowerFloor.generators).firstOrNull()?.let {
        elevatorFloor.chips.remove(it)
        lowerFloor.chips.add(it)
        return true
    }

    if (elevatorFloor.chips.size == 1 && elevatorFloor.generators.size == 1) {
        lowerFloor.generators.add(elevatorFloor.generators.removeFirst())
        return true
    }

    return false
}