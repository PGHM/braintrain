package com.houston.cow_manager.cowmanager

import android.os.Parcel
import android.os.Parcelable
import java.lang.IllegalArgumentException
import java.util.*

data class Cow(val name: String, val type: Type, val color: Int) : Parcelable {

    enum class Type {
        HEREFORD,
        ANGUS,
        MUSTIKKI;

        override fun toString(): String {
            return super.toString().toLowerCase(Locale.getDefault()).capitalize()
        }

        companion object {
            fun fromString(value: String): Cow.Type? {
                try {
                    return valueOf(value.toUpperCase(Locale.getDefault()))
                } catch (e: IllegalArgumentException) {
                    return null
                }
            }
        }
    }

    // Parcelable implementation
    constructor(parcel: Parcel): this(
        parcel.readString(),
        parcel.readSerializable() as Type,
        parcel.readInt()
    )

    override fun writeToParcel(parcel: Parcel, flags: Int) {
        parcel.writeString(name)
        parcel.writeSerializable(type)
        parcel.writeInt(color)
    }

    override fun describeContents(): Int {
        return 0
    }

    companion object CREATOR : Parcelable.Creator<Cow> {
        override fun createFromParcel(parcel: Parcel): Cow {
            return Cow(parcel)
        }

        override fun newArray(size: Int): Array<Cow?> {
            return arrayOfNulls(size)
        }
    }
}