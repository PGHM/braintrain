package com.houston.cow_manager.cowmanager

import android.os.Parcel
import android.os.Parcelable

data class Cow(val name: String, val type: Type, val color: Int) : Parcelable {

    enum class Type {
        HEREFORD,
        ANGUS,
        MUSTIKKI
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