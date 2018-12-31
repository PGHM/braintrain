import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'AddTrackScreen.dart';

class OrganizerScreen extends StatefulWidget {
  @override
  _OrganizerScreenState createState() => _OrganizerScreenState();
}

class _OrganizerScreenState extends State<OrganizerScreen> {
  final _tracks = <String>[];

  @override
  void initState() {
    super.initState();

    _getTracks();
  }

  Future<void> _getTracks() async {
    final snapshot = await Firestore.instance.collection('tracks').getDocuments();
    setState(() {
      _tracks.clear();
      _tracks.addAll(snapshot.documents.map((document) => document.data['name']));
    });
  }

  void _addTrack() {
    Navigator.of(context).push(
      new MaterialPageRoute<void>(
        fullscreenDialog: true,
        builder: (BuildContext context) {
          return AddTrackScreen();
        },
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ListView(
        children: _tracks.map((username) => Text(username)).toList(),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _addTrack,
        child: Icon(Icons.add),
      ),
    );
  }
}
