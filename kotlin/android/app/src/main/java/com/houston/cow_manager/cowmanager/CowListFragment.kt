package com.houston.cow_manager.cowmanager

import android.content.Context
import android.graphics.Rect
import android.os.Bundle
import android.support.v4.app.Fragment
import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import java.lang.IllegalStateException

private const val TITLE_KEY = "title"
private const val DATA_KEY = "data"

interface CowListListener {
    fun selectedCowAt(index: Int)
}

class CowListFragment : Fragment() {
    private lateinit var title: String
    private lateinit var data: List<Cow>
    private lateinit var recyclerView: RecyclerView
    private var listener: CowListListener? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val title = arguments?.getString(TITLE_KEY)
        val data = arguments?.getParcelableArrayList<Cow>(DATA_KEY)

        if (title == null || data == null) { throw IllegalStateException() }

        this.title = title
        this.data = data
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        recyclerView =
            inflater.inflate(R.layout.fragment_cow_list, container, false) as RecyclerView
        recyclerView.adapter = CowListAdapter(recyclerView.context, data)

        val padding = resources.getDimension(R.dimen.cow_list_padding).toInt()
        val decoration = MarginItemDecoration(padding)
        recyclerView.addItemDecoration(decoration)

        return recyclerView
    }

    override fun onAttach(context: Context) {
        super.onAttach(context)

        if (context is CowListListener) {
            listener = context
        }
    }

    override fun onDetach() {
        super.onDetach()
        listener = null
    }

    companion object {
        fun newInstance(title: String, data: ArrayList<Cow>) =
            CowListFragment().apply {
                arguments = Bundle().apply {
                    putString(TITLE_KEY, title)
                    putParcelableArrayList(DATA_KEY, data)
                }
            }
    }
}

private class MarginItemDecoration(private val spaceHeight: Int) : RecyclerView.ItemDecoration() {
    override fun getItemOffsets(
        outRect: Rect,
        view: View,
        parent: RecyclerView,
        state: RecyclerView.State
    ) {
        with(outRect) {
            if (parent.getChildAdapterPosition(view) == 0) {
                top = spaceHeight
            }
            left =  spaceHeight
            right = spaceHeight
            bottom = spaceHeight
        }
    }
}
