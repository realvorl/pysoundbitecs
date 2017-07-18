var soundBiteServer = "http://localhost:8080"
//var soundBiteServer = "http://10.90.212.26:8080"

var BuzzerButton = React.createClass({
	getInitialState() {
		return {count: 0}
	},

	handlePlay() {
		var bThis = this;
		var biteId = bThis.props.order;
		var url = soundBiteServer + "/soundBite/"+biteId;
		$.getJSON(url, function(data) {
		 bThis.setState({count: (bThis.state.count + 1) })
		})
	},

	render() {
		return <div className="bimmel" onClick={this.handlePlay}>
			<h3>{this.props.title}</h3>
			<p>{this.props.children}</p>
			<img src={"../server/img/"+this.props.img} alt=":o"></img>
			<span>
				<span className="counter"> #{this.state.count} </span>
			</span>
		</div>
	}
})

var SwitchBoard = React.createClass({
	getInitialState(){
		var bThis = this;
		var sBites = $.getJSON(soundBiteServer+"/soundBites", function(data) {
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
				return <BuzzerButton key={i} order={soundBite.id} title={soundBite.title} img={soundBite.img}> {soundBite.title}</BuzzerButton>
			})}
		</div>
	}
})

ReactDOM.render(<SwitchBoard samples={11}/>,
document.getElementById('root'))
