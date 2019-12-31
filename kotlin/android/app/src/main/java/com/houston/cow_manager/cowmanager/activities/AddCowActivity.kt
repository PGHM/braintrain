package com.houston.cow_manager.cowmanager.activities

import android.app.Activity
import android.content.Context
import android.content.Intent
import android.graphics.Color
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.AttributeSet
import android.util.Log
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.EditText
import android.widget.Spinner
import com.houston.cow_manager.cowmanager.Cow
import com.houston.cow_manager.cowmanager.R
import kotlinx.android.synthetic.main.activity_add_cow.*
import java.util.*

class AddCowActivity : AppCompatActivity() {

    private lateinit var typeSpinner: Spinner
    private lateinit var colorSpinner: Spinner

    companion object {
        const val RESULT_COW_KEY = "result_cow_key"
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_add_cow)

        typeSpinner = findViewById<Spinner>(R.id.type_select)
        colorSpinner = findViewById<Spinner>(R.id.color_select)

        ArrayAdapter.createFromResource(
            this,
            R.array.cow_color_choices,
            android.R.layout.simple_spinner_item
        ).apply {
            setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
            colorSpinner.adapter = this
        }

        ArrayAdapter(this, android.R.layout.simple_spinner_item, Cow.Type.values()).apply {
            setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
            typeSpinner.adapter = this
        }
    }

    fun save(view: View) {
        val nameField = findViewById<EditText>(R.id.name_select)
        val nameValue = nameField.text.toString()
        val name = if (nameValue != "") nameValue else getString(R.string.add_cow_name_hint)

        val type = Cow.Type.fromString(typeSpinner.selectedItem.toString()) ?: Cow.Type.MUSTIKKI
        val color = when(colorSpinner.selectedItem.toString()) {
            "Red" -> getColor(R.color.cowRed)
            "Black" -> Color.BLACK
            "Green" -> getColor(R.color.cowGreen)
            else -> Color.WHITE
        }

        val result = Intent()
        result.putExtra(RESULT_COW_KEY, Cow(name, type, color))
        setResult(Activity.RESULT_OK, result)
        finish()
    }
}
