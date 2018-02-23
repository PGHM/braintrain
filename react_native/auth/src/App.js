import React, { Component } from 'react';
import { View, Text } from 'react-native';
import Header from './components/common/Header';

class App extends Component {
  render() {
    return (
      <View>
        <Header headerText='Authentication' />
        <Text>Foobar</Text>
      </View>
    );
  };
}

export default App;