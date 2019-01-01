import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:orienteering_helper/models/Track.dart';

class EditTrackScreen extends StatefulWidget {
  final Track _track;

  EditTrackScreen(this._track);

  @override
  _EditTrackScreenState createState() => _EditTrackScreenState();
}

class _EditTrackScreenState extends State<EditTrackScreen> {
  final trackNameController = TextEditingController();

  void _addTrack() async {
    await Firestore.instance.collection('tracks').add({"name": trackNameController.text, "control_points": []});
    Navigator.of(context).pop(true);
  }

  void _updateTrack() async {
    Firestore.instance
        .collection('tracks').reference()
        .where("name", isEqualTo: widget._track.name)
        .getDocuments()
        .then((QuerySnapshot snapshot) {
      snapshot.documents.first.reference.updateData({"name": trackNameController.text, "control_points": []});
      Navigator.of(context).pop(true);
    });
  }

  @override
  void initState() {
    super.initState();

    if (widget._track != null) trackNameController.text = widget._track.name;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: widget._track == null ? Text("Add a new track") : Text("Edit the track"),
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
                onPressed: widget._track == null ? _addTrack : _updateTrack,
              ),
            ),
          ],
        )));
  }
}
