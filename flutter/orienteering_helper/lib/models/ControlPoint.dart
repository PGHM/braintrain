class ControlPoint extends Object {
  final String name;
  final String code;
  final double lat;
  final double lon;

  const ControlPoint(this.name, this.code, this.lat, this.lon);

  ControlPoint.fromJson(Map json)
      : name = json['name'],
        code = json['code'],
        lat = json['lat'],
        lon = json['lon'];

  Map toJson() {
    return {
      'name': name,
      'code': code,
      'lat': lat,
      'lon': lon,
    };
  }
}
