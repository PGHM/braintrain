import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:orienteering_helper/screens/AddTrackScreen.dart';

class OrganizerScreen extends StatefulWidget {
  @override
  _OrganizerScreenState createState() => _OrganizerScreenState();
}

class _OrganizerScreenState extends State<OrganizerScreen> with AutomaticKeepAliveClientMixin<OrganizerScreen> {
  @override
  bool get wantKeepAlive => true;

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

  void _addTrack() async {
    final result = await Navigator.of(context).push(
      new MaterialPageRoute<bool>(
        fullscreenDialog: true,
        builder: (BuildContext context) {
          return AddTrackScreen();
        },
      ),
    );

    if (result) {
      _getTracks();
    }
  }

  void _removeTrack(String trackName) async {
    showDialog<void>(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text("Remove track '$trackName'"),
          actions: <Widget>[
            FlatButton(
              child: Text('Yes'),
              onPressed: () {
                Firestore.instance
                    .collection('tracks').reference()
                    .where("name", isEqualTo: trackName)
                    .getDocuments()
                    .then((QuerySnapshot snapshot) {
                  snapshot.documents.first.reference.delete();
                  _getTracks();
                  Navigator.of(context).pop();
                });
              },
            ),
            FlatButton(
              child: Text('No'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ListView(
        children: ListTile.divideTiles(
          context: context,
          tiles: _tracks.map((trackName) {
            return ListTile(
              leading: Icon(Icons.edit),
              title: Text(trackName),
              onLongPress: () => _removeTrack(trackName),
            );
          }),
        ).toList(),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _addTrack,
        child: Icon(Icons.add),
      ),
    );
  }
}
