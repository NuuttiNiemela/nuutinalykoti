import React, { useState, useEffect } from 'react'
import axios from 'axios';


const App = props => {

    useEffect(() => {
        axios.get('/api/hello')
            .then(res => setState(res.data))
    }, [])

    const light = (what) => {
        axios.get('/0/' + what)
            .then(res => setState({light: res}))
    }

    const [state, setState] = useState('')
    return(
        <div>
            <button onClick={() => light('0')}>Pois</button>
            <button onClick={() => light('1')}>Päälle</button>
            <button onClick={() => light('red')}>Punainen</button>
            <button onClick={() => light('green')}>Vihreä</button>
            <button onClick={() => light('blue')}>Sininen</button>
            <button onClick={() => light('yellow')}>Keltainen</button>
            <button onClick={() => light('janne')}>Janne</button>
        </div>
    )
};
export default App;