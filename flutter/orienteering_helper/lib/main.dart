import 'package:flutter/material.dart';
import 'UserScreen.dart';
import 'OrganizerScreen.dart';

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
      home: DefaultTabController(
        length: 2,
        child: Scaffold(
          appBar: AppBar(
            bottom: TabBar(
              tabs: [
                Tab(icon: Icon(Icons.account_circle)),
                Tab(icon: Icon(Icons.add_location)),
              ],
            ),
            title: Text("Orienteering Helper"),
          ),
          body: TabBarView(
            children: [
              UserScreen(),
              UserScreen(),
            ],
          ),
        ),
      ),
    );
  }
}