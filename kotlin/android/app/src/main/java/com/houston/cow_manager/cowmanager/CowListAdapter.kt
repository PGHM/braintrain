package com.houston.cow_manager.cowmanager

import android.content.Context
import android.content.res.ColorStateList
import android.graphics.drawable.Drawable
import android.support.v4.widget.ImageViewCompat
import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.LinearLayout
import android.widget.TextView

class CowListAdapter(private val context: Context, private val cows: ArrayList<Cow>)
    : RecyclerView.Adapter<CowListAdapter.CowViewHolder>() {

    class CowViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        private val logoView: ImageView = itemView.findViewById(R.id.logo)
        private val nameView: TextView = itemView.findViewById(R.id.name)
        private val contentView: LinearLayout = itemView.findViewById(R.id.content_view)

        fun bind(cow: Cow, background: Drawable?) {
            nameView.text = cow.name
            ImageViewCompat.setImageTintList(logoView, ColorStateList.valueOf(cow.color))
            contentView.background = background
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CowViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.row_cow_info, parent, false)
        return CowViewHolder(view)
    }

    override fun onBindViewHolder(holder: CowViewHolder, position: Int) {
        val background =
            if (position % 2 == 0) context.getDrawable(R.drawable.cow_info_border)
            else context.getDrawable(R.drawable.cow_info_border_coloured)

        holder.bind(cows[position], background)
    }

    override fun getItemCount() = cows.size
}