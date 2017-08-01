import React from 'react';
import logo from './logo.svg'
import jquery from 'jquery'
import './App.css'
import BuzzerButton from './BuzzerButton'

var soundBiteServer = "http://localhost:8080"
//var soundBiteServer = "http://10.90.212.26:8080"
var SwitchBoard = React.createClass({
  getInitialState(){
    var bThis = this;
    var sBites = jquery.getJSON(soundBiteServer + "/soundBites", function(data) {
     bThis.setState({soundBites: data})
    })
    return {
      soundBites: [
        {id:0, title: 'Unable to reach'},
        {id:1, title: 'webservice'},
        {id:2, title: 'http://server:8080/soundBites'},
        {id:3, title: 'start it up and refresh the site'}
      ]
    }
  },
  render(){
    return <div className='board'>
      {this.state.soundBites.map((soundBite, i) => {
        return <BuzzerButton 
         key={i} 
         order={soundBite.id} 
         title={soundBite.title} 
         img={soundBite.img}> 
          {soundBite.title}
              </BuzzerButton>
      })}
    </div>
  }
})

export default SwitchBoard;
