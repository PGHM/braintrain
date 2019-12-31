package com.houston.cow_manager.cowmanager.activities

import android.app.Activity
import android.content.Intent
import android.graphics.Color
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import com.houston.cow_manager.cowmanager.Cow
import com.houston.cow_manager.cowmanager.R

class AddCowActivity : AppCompatActivity() {

    companion object {
        const val RESULT_COW_KEY = "result_cow_key"
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_add_cow)

        val result = Intent()
        result.putExtra(
            RESULT_COW_KEY,
            Cow("It is me, Mario!", Cow.Type.HEREFORD, Color.BLACK)
        )
        setResult(Activity.RESULT_OK, result)
        finish()
    }
}
