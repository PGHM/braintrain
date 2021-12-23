import java.io.File

const val lowResultValue = 17
const val highResultValue = 61
val botRegex = """bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)""".toRegex()
val valueRegex = """value (\d+) goes to bot (\d+)""".toRegex()

enum class NodeType(val readableName: String) {
    BOT("bot"),
    OUTPUT("output");

    companion object {
        fun fromReadableName(readableName: String) = values().first { it.readableName == readableName }
    }
}

data class NodeID(val numericID: Int, val type: NodeType)

sealed class Node {
    abstract val nodeID: NodeID
    abstract fun addValue(value: Int, graph: MutableMap<NodeID, Node>)
}

data class Output( override val nodeID: NodeID, var value: Int?) : Node() {
    override fun addValue(value: Int, graph: MutableMap<NodeID, Node>) {
        this.value = value
    }
}

data class Bot(
    override val nodeID: NodeID,
    var values: List<Int>,
    val lowTargetID: NodeID,
    val highTargetID: NodeID
) : Node() {
    override fun addValue(value: Int, graph: MutableMap<NodeID, Node>) {
        values = (values + value).sorted()

        if (values.size < 2) return

        val lowTarget = getTarget(lowTargetID, graph)
        val highTarget = getTarget(highTargetID, graph)
        val lowValue = values[0]
        val highValue = values[1]

        if (lowValue == lowResultValue && highValue == highResultValue) {
            println("Bot that compares ${lowResultValue} and ${highResultValue} is ${nodeID.numericID}")
        }

        lowTarget.addValue(lowValue, graph)
        highTarget.addValue(highValue, graph)
    }

    private fun getTarget(targetID: NodeID, graph: MutableMap<NodeID, Node>): Node {
        graph[targetID]?.let { return it }

        Output(targetID, null).also {
            graph[targetID] = it
        }.let {
            return it
        }
    }
}

fun main() {
    val input = File("day_10/input.txt").readLines().sorted()
    val graph = parseInput(input, HashMap())
    val output0Value = (graph[NodeID(0, NodeType.OUTPUT)] as Output).value!!
    val output1Value = (graph[NodeID(1, NodeType.OUTPUT)] as Output).value!!
    val output2Value = (graph[NodeID(2, NodeType.OUTPUT)] as Output).value!!
    println("Values from outputs 0, 1, 2 multiplied are ${output0Value * output1Value * output2Value}")
}

tailrec fun parseInput(input: List<String>, currentGraph: MutableMap<NodeID, Node>): MutableMap<NodeID, Node> {
    val instruction = input.firstOrNull() ?: return currentGraph

    updateGraphFromInstruction(instruction, currentGraph)
    return parseInput(input.drop(1), currentGraph)
}

fun updateGraphFromInstruction(instruction: String, graph: MutableMap<NodeID, Node>) {
    botRegex.matchEntire(instruction)?.let {
        val (botID, lowTargetType, lowTargetID, highTargetType, highTargetID) = it.destructured
        val botNodeID = NodeID(botID.toInt(), NodeType.BOT)
        val lowTargetNodeID = NodeID(lowTargetID.toInt(), NodeType.fromReadableName(lowTargetType))
        val highTargetNodeID = NodeID(highTargetID.toInt(), NodeType.fromReadableName(highTargetType))
        graph[botNodeID] = Bot(botNodeID, listOf(), lowTargetNodeID, highTargetNodeID)
        return
    }

    valueRegex.matchEntire(instruction)?.let {
        val (value, targetBotID) = it.destructured
        val targetNode = graph[NodeID(targetBotID.toInt(), NodeType.BOT)] ?: return
        targetNode.addValue(value.toInt(), graph)
    }
}