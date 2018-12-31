import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class AddTrackScreen extends StatefulWidget {
  @override
  _AddTrackScreenState createState() => _AddTrackScreenState();
}

class _AddTrackScreenState extends State<AddTrackScreen> {

  Future<void> _addTrack() async {
//TODO:    final snapshot = await Firestore.instance.collection('tracks').add();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Orienteering Helper"),
      ),
      body: Center(child: Text("HERE WE WILL ADD TRACKS, YAY"),)
    );
  }
}
