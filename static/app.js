const e = React.createElement

class Tile extends React.Component {
  constructor(props) {
    super(props)
  }

  render() {
    return e('th', {className: 'game-tile'}, this.props.value)
  }
}

class Board extends React.Component {
  constructor(props, size) {
    super(props)
    this.state = {size}

    // tiles = [...]
  }

  // TODO: Game logic
  initializeTiles() {
    // TODO
  }

  tilesSwapped() {
    // TODO
  }

  trySwap() {
    // TODO
  }

  componentDidMount() {
    // TODO:
    //  init game
    //    - get game data from server
  }

  componentWillUnmount() {
    // TODO:
  }

  render() {
//     const n = this.state.size
//     const view = Array
//       .from({length: n})
//       .map((_, i) => {
//         return e('tr', {}, Array
//           .from({length: n}))
//           .map((_, j) => {
//             return e(Tile, {value: i*n+j+1})
//           })
//       })
// debugger;
//     return e('table', {id:'game-board'}, view)

    // this.props.children...
  }
}

class Hello extends React.Component {
  constructor(props) {
    super(props)
    this.state = {date: new Date()}
  }

  componentDidMount() {
    this.timerID = setInterval(() => {
      this.setState({
        date: new Date()
      })
    }, 1000)
  }

  componentWillUnmount() {
    clearInterval(this.timerID)
  }

  tick() {
    this.setState({
      date: new Date()
    })
  }

  render() {
    return e('div', {}, [
      e('h1', {key: 0}, this.props.name),
      e('h2', {key: 1}, `The time is: ${this.state.date.toTimeString()}`)
    ])
  }
}