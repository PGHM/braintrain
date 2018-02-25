import React, { Component } from 'react';
import { Text } from 'react-native';
import firebase from 'firebase';
import Button from './common/Button';
import Card from './common/Card';
import CardSection from './common/CardSection';
import Input from './common/Input';
import Spinner from './common/Spinner';

class LoginForm extends Component {

  state = { email: '', password: '', error: '', loading: false };

  onButtonPress() {
    this.setState({ error: '', loading: true });

    firebase.auth().signInWithEmailAndPassword(this.state.email, this.state.password)
      .then(this.onLoginSuccess.bind(this))
      .catch(() => {
        firebase.auth().createUserWithEmailAndPassword(this.state.email, this.state.password)
          .then(this.onLoginSuccess.bind(this))
          .catch(this.onLoginFail.bind(this));
      });
  }

  onLoginFail() {
    this.setState({ error: 'Authentication failed ', loading: false });
  }

  onLoginSuccess() {
    this.setState({ error: '', loading: false, email: '', password: '' });
  }

  renderButton() {
    if (this.state.loading) {
      return <Spinner size='small' />;
    }

    return <Button onPress={this.onButtonPress.bind(this)}>Log in</Button>;
  }

  render() {
    return (
      <Card>
        <CardSection>
          <Input
            label='Email:'
            placeholder='john.doe@jane.com'
            value={this.state.email}
            onChangeText={email => this.setState({ email })}
          />
        </CardSection>

        <CardSection>
          <Input
            secureTextEntry
            label='Password:'
            value={this.state.password}
            onChangeText={password => this.setState({ password })}
          />
        </CardSection>
        
        <Text style={styles.errorTextStyle}>
          {this.state.error}
        </Text>

        <CardSection>
          {this.renderButton()}
        </CardSection>
      </Card>
    );
  }
}

const styles = {
  errorTextStyle: {
    fontSize: 20,
    alignSelf: 'center',
    color: 'red'
  }
};

export default LoginForm;
