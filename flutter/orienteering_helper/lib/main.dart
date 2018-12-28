import 'package:flutter/material.dart';
import 'UserScreen.dart';

void main() => runApp(OrienteeringHelperApp());

class OrienteeringHelperApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Orienteering Helper',
      theme: ThemeData(
        brightness: Brightness.dark,
        primarySwatch: Colors.red,
        primaryColor: Colors.red,
        accentColor: Colors.redAccent,
        accentIconTheme: IconThemeData(color: Colors.black),
      ),
      home: UserScreen(),
    );
  }
}