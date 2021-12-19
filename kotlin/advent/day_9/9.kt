import java.io.File

val instructionRegex = """\((\d+)x(\d+)\)""".toRegex()

fun main() {
    val input = File("day_9/input.txt").readText()
    println("Length of the once decompressed input is ${decompressedLength(input, true, 0)}")
    println("Length of the fully decompressed input is ${decompressedLength(input, false, 0)}")
}

fun decompressedLength(compressedInput: String, decompressOnce: Boolean, totalLength: Long): Long {
    val matchResult = instructionRegex.find(compressedInput)
    if (matchResult == null) {
        return totalLength + compressedInput.length
    }

    val (compressedPartLength, compressedPartRepeatAmount) = matchResult.destructured
    val compressedPartStartIndex = matchResult.range.endInclusive + 1
    val compressedPartEndIndex = matchResult.range.endInclusive + compressedPartLength.toInt()
    val compressedPart = compressedInput.slice(compressedPartStartIndex..compressedPartEndIndex)

    val decompressedPartLength = if (decompressOnce) {
        compressedPart.length * compressedPartRepeatAmount.toLong()
    } else {
        decompressedLength(compressedPart, false, 0) * compressedPartRepeatAmount.toLong()
    }

    return decompressedLength(
        compressedInput.drop(compressedPartEndIndex + 1),
        decompressOnce,
        totalLength + matchResult.range.first + decompressedPartLength
    )
}
