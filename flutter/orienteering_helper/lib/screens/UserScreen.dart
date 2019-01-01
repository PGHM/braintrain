import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:orienteering_helper/models/Track.dart';

class UserScreen extends StatefulWidget {
  @override
  _UserScreenState createState() => _UserScreenState();
}

class _UserScreenState extends State<UserScreen> with AutomaticKeepAliveClientMixin<UserScreen> {

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

  @override
  Widget build(BuildContext context) {
    return RefreshIndicator(
      onRefresh: _getTracks,
      child: ListView(
        physics: const AlwaysScrollableScrollPhysics(),
        children: ListTile.divideTiles(
          context: context,
          tiles: _tracks.map((track) {
            track.toJson();
            return ListTile(
              leading: Icon(Icons.linear_scale),
              title: Text(track.name),
            );
          }),
        ).toList(),
      ),
    );
  }
}
