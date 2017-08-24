import React from 'react';
import logo from './logo.svg'
import Draggable from 'react-draggable'
import jquery from 'jquery'
import './App.css'

var soundBiteServer = "http://localhost:8080"
var defaultImg = 'default.png'

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
  handleRemove() {
    console.log("removing" + this.props.title);
    this.setState({off: true});
  },

  render() {
    if (this.state.off) return null;
    return (
      <Draggable>
      <div className="bimmel" >
      <h3>{this.props.title}</h3>
      <img src={"http://localhost:8080/static/images/" + this.props.img} onClick={this.handlePlay}></img>
      <span>
        <span className="counter"> #{this.state.count} </span>
        <button onClick={this.handleRemove}> x </button>
      </span>
    </div>
    </Draggable>
    )
  }
})

export default BuzzerButton
