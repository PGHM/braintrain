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
        title: Text("Orienteering Helper"),
      ),
        body: Center(
            child: Column(
              children: <Widget>[
                Text("Name of the track:"),
                TextField(
                  controller: trackNameController,
                ),
                IconButton(
                  icon: Icon(Icons.save),
                  onPressed: _addTrack,
                ),
              ],
            )
        )
    );
  }
}
