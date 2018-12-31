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
        accentColor: Colors.white,
      ),
      home: DefaultTabController(
        length: 2,
        child: Scaffold(
          appBar: AppBar(
            bottom: TabBar(
              tabs: [
                Tab(icon: Icon(Icons.map)),
                Tab(icon: Icon(Icons.add_location)),
              ],
            ),
            title: Text("Orienteering Helper"),
          ),
          body: TabBarView(
            physics: const NeverScrollableScrollPhysics(),
            children: [
              UserScreen(),
              OrganizerScreen(),
            ],
          ),
        ),
      ),
    );
  }
}