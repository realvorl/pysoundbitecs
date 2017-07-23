import React from 'react';
import logo from './logo.svg'
import defaultImg from './images/default.png'
import Draggable from 'react-draggable'
import jquery from 'jquery'
import './App.css'

var soundBiteServer = "http://localhost:8080"

var BuzzerButton = React.createClass({
  getInitialState() {
    return {count: 0}
  },

  handlePlay() {
    var bThis = this;
    var biteId = bThis.props.order;
    var url = soundBiteServer+"/soundBite/"+biteId;
    jquery.getJSON(url, function(data) {
     bThis.setState({count: (bThis.state.count + 1) })
    })
  },

  render() {
    return (
      <Draggable>
      <div className="bimmel" onClick={this.handlePlay}>
      <h3>{this.props.title}</h3>
      <p>{this.props.children}</p>
      <img src={defaultImg} alt={this.props.img}></img>
      <span>
        <span className="counter"> #{this.state.count} </span>
      </span>
    </div>
    </Draggable>
    )
  }
})

export default BuzzerButton