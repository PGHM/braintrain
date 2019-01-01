import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:orienteering_helper/screens/EditTrackScreen.dart';
import 'package:orienteering_helper/models/Track.dart';

class OrganizerScreen extends StatefulWidget {
  @override
  _OrganizerScreenState createState() => _OrganizerScreenState();
}

class _OrganizerScreenState extends State<OrganizerScreen> with AutomaticKeepAliveClientMixin<OrganizerScreen> {
  @override
  bool get wantKeepAlive => true;

  final _tracks = <Track>[];

  @override
  void initState() {
    super.initState();

    _getTracks();
  }

  Future<void> _getTracks() async {
    final snapshot = await Firestore.instance.collection('tracks').getDocuments();
    setState(() {
      _tracks.clear();
      _tracks.addAll(snapshot.documents.map((document) => Track.fromJson(document.data)));
    });
  }

  void _addTrack() async {
    _editTrack(null);
  }

  void _editTrack(Track track) async {
    final result = await Navigator.of(context).push(
      new MaterialPageRoute<bool>(
        fullscreenDialog: true,
        builder: (BuildContext context) {
          return EditTrackScreen(track);
        },
      ),
    );

    if (result != null && result) {
      _getTracks();
    }
  }

  void _removeTrack(Track track) async {
    showDialog<void>(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text("Remove track '${track.name}'?"),
          actions: <Widget>[
            FlatButton(
              child: Text('Yes'),
              onPressed: () {
                Firestore.instance
                    .collection('tracks').reference()
                    .where("name", isEqualTo: track.name)
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
          tiles: _tracks.map((track) {
            return ListTile(
              leading: Icon(Icons.edit),
              title: Text(track.name),
              onLongPress: () => _removeTrack(track),
              onTap: () => _editTrack(track),
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
