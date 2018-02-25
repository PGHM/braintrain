import firebase from 'firebase';
import React, { Component } from 'react';
import { View } from 'react-native';
import Header from './components/common/Header';
import Button from './components/common/Button';
import LoginForm from './components/LoginForm';
import Spinner from './components/common/Spinner';
import Card from './components/common/Card';
import CardSection from './components/common/CardSection';

class App extends Component {

  state = { loggedIn: null };

  componentWillMount() {
    const config = {
      apiKey: 'AIzaSyAHANpzt3JIz1vgpK2zl8-FFD-lK9C6z2w',
      authDomain: 'auth-33a4e.firebaseapp.com',
      databaseURL: 'https://auth-33a4e.firebaseio.com',
      projectId: 'auth-33a4e',
      storageBucket: 'auth-33a4e.appspot.com',
      messagingSenderId: '993900758549'
    };

    firebase.initializeApp(config);
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        this.setState({ loggedIn: true });
      } else {
        this.setState({ loggedIn: false });
      }
    });
  }

  renderContent() {
    switch (this.state.loggedIn) {
      case true:
        return (
          <Card>
            <CardSection>
              <Button onPress={() => firebase.auth().signOut()}>Log out</Button>
            </CardSection>
          </Card>
        );
      case false:
        return <LoginForm />;
      default:
        return <Spinner />;
    }
  }

  render() {
    return (
      <View>
        <Header headerText='Authentication' />
        {this.renderContent()}
      </View>
    );
  }
}

export default App;
