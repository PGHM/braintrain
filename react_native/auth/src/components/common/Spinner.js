import React from 'react';
import { View, ActivityIndicator } from 'react-native';

const Spinner = ({ size }) => {  
  return (
    <View style={styles.viewStyle}>
      <ActivityIndicator size={size || 'large'} />
    </View>
  );
};

const styles = {
  viewStyle: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  }
};

export default Spinner;
