import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class AddTrackScreen extends StatefulWidget {
  @override
  _AddTrackScreenState createState() => _AddTrackScreenState();
}

class _AddTrackScreenState extends State<AddTrackScreen> {

  final trackNameController = TextEditingController();

  Future<void> _addTrack() async {
    await Firestore.instance.collection('tracks').add({"name" : trackNameController.text });
    Navigator.of(context).pop(true);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Add a new track"),
      ),
        body: Center(
            child: Column(
              children: <Widget>[
                Padding(
                  padding: EdgeInsets.only(top: 10),
                  child: Text("Name:"),
                ),
                Padding(
                  padding: EdgeInsets.only(top: 10, left: 10, right: 10),
                  child: Container(
                    child: TextField(
                      controller: trackNameController,
                    ),
                    constraints: BoxConstraints.tightFor(width: 250),
                  ),
                ),
                Padding(
                  padding: EdgeInsets.only(top: 10),
                  child: RaisedButton(
                    child: Text("Save"),
                    onPressed: _addTrack,
                  ),
                ),
              ],
            )
        )
    );
  }
}
