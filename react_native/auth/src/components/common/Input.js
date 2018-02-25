import React from 'react';
import { Text, View, TextInput } from 'react-native';

const Input = ({ label, value, onChangeText, placeholder, secureTextEntry }) => {
  const { textStyle, viewStyle, textInputStyle } = styles;
  
  return (
    <View style={viewStyle}>
      <Text style={textStyle}>{label}</Text>
      <TextInput
        secureTextEntry={secureTextEntry}
        value={value}
        onChangeText={onChangeText}
        style={textInputStyle}
        autoCorrect={false}
        placeholder={placeholder}
      />
    </View>
  );
};

const styles = {
  textInputStyle: {
    height: 20, 
    width: 100,
    color: '#000',
    paddingRight: 5,
    paddingLeft: 5,
    fontSize: 18,
    lineHeight: 23,
    flex: 2
  },

  textStyle: {
    fontSize: 18,
    paddingLeft: 20,
    flex: 1
  },

  viewStyle: {
    height: 40,
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center'
  }
};

export default Input;
