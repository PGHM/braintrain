import 'ControlPoint.dart';

class Track extends Object {
  final String name;
  final List<ControlPoint> controlPoints;

  const Track(this.name, this.controlPoints);

  Track.fromJson(Map json)
      : this.name = json['name'],
        this.controlPoints =
            json['control_points'].map<ControlPoint>((pointJson) => ControlPoint.fromJson(pointJson)).toList();

  Map toJson() {
    return {
      'name': name,
      'control_points': controlPoints.map((controlPoint) => controlPoint.toJson()),
    };
  }
}
