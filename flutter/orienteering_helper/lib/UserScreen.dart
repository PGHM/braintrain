import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'dart:async';

class UserScreen extends StatefulWidget {
  @override
  _UserScreenState createState() => _UserScreenState();
}

class _UserScreenState extends State<UserScreen> {
  final _users = <String>[];

  @override
  void initState() {
    super.initState();

    _getTracks();
  }

  Future<void> _getTracks() async {
    final snapshot = await Firestore.instance.collection('tracks').getDocuments();
    setState(() {
      _users.clear();
      _users.addAll(
          snapshot.documents.map((document) => document.data['name']));
    });
  }

  @override
  Widget build(BuildContext context) {
    return RefreshIndicator(
      onRefresh: _getTracks,
      child: ListView(
        physics: const AlwaysScrollableScrollPhysics(),
        children: _users.map((username) => Text(username)).toList(),
      ),
    );
  }
}
