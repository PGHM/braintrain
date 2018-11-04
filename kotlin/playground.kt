/**
 * You can edit, run, and share this code. 
 * play.kotlinlang.org 
 */

const val LIMIT = 10000

fun main() {
	val fibonacciList = ArrayList<Int>()
	fibonacciList.add(1)
    fibonacciList.add(1)
    println(fibonacci(fibonacciList))
    
    val values = arrayListOf(1, 2, 3)
    println(foldSum(Int::plus, values, 0))
}

tailrec fun fibonacci(series: ArrayList<Int>): ArrayList<Int> {
    if (series.size < 2) { return series }
    
    val lastElement = series[series.size - 1]
    val secondLastElement = series[series.size - 2]
    if (lastElement + secondLastElement > LIMIT) { return series }
    
    series.add(lastElement + secondLastElement)
    return fibonacci(series)
}

tailrec fun foldSum(op: (Int, Int) -> Int, values: ArrayList<Int>, currentValue: Int): Int {
    if (values.isEmpty()) { return currentValue }
    
    val lastValue = values.last()
    values.removeAt(values.size - 1)
    return foldSum(op, values, op(currentValue, lastValue))
}
