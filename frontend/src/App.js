import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor() {
      super();
      this.state = { items: [] };
  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <ul>
           {this.state.items.map((item)=><li key={item.id}>{item.name}</li>)}
        </ul>
      </div>
    );
  }

  componentDidMount() {
    fetch(`http://localhost:8000/api/profiles/`, {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      }
    }).then((response) => response.json())
      .then((responseJson) => {
          console.log(responseJson);
          this.setState({items:responseJson});
        }
    );
  }
}

export default App;
