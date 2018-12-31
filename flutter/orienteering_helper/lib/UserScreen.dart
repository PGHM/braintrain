import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class UserScreen extends StatefulWidget {
  @override
  _UserScreenState createState() => _UserScreenState();
}

class _UserScreenState extends State<UserScreen> {
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

  @override
  Widget build(BuildContext context) {
    return RefreshIndicator(
      onRefresh: _getTracks,
      child: ListView(
        physics: const AlwaysScrollableScrollPhysics(),
        children: ListTile.divideTiles(
          context: context,
          tiles: _tracks.map((trackName) {
            return ListTile(
              leading: Icon(Icons.linear_scale),
              title: Text(trackName),
            );
          }),
        ).toList(),
      ),
    );
  }
}
