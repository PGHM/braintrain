package com.houston.cow_manager.cowmanager

import android.os.Bundle
import android.support.v7.app.AppCompatActivity

import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity(), CowListListener {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        if (savedInstanceState != null) return

        val cows = arrayListOf(
            Cow("Mansikki", Cow.Type.HEREFORD, getColor(R.color.cowGreen)),
            Cow("Mustikki", Cow.Type.ANGUS, getColor(R.color.cowRed)),
            Cow("Helmikki", Cow.Type.MUSTIKKI, getColor(R.color.cowRed)),
            Cow("Ansikki", Cow.Type.ANGUS, getColor(R.color.cowRed)),
            Cow("Julmettu", Cow.Type.MUSTIKKI, getColor(R.color.cowGreen)),
            Cow("Vimmattu", Cow.Type.ANGUS, getColor(R.color.cowGreen)),
            Cow("Kammattu", Cow.Type.MUSTIKKI, getColor(R.color.cowRed)),
            Cow("Rasvattu", Cow.Type.ANGUS, getColor(R.color.cowGreen)),
            Cow("Kuningas", Cow.Type.HEREFORD, getColor(R.color.cowRed)),
            Cow("Kuningatar", Cow.Type.HEREFORD, getColor(R.color.cowGreen))
        )
        val cowList = CowListFragment.newInstance(getString(R.string.cow_list_title), cows)
        supportFragmentManager.beginTransaction().add(R.id.cow_list_container, cowList).commit()

        add_button.setOnClickListener {
            //TODO: Open add new cow activity
        }
    }

    // CowListListener implementation
    override fun selectedCowAt(index: Int) {
        //TODO: Open cow details activity
    }
}
