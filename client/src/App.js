import React, { useState, useEffect } from 'react'
import axios from 'axios';
import ReactBootstrapSlider from 'react-bootstrap-slider';

const App = props => {
    const [huone, setHuone] = useState('Olohuone')
    const [brightness, setBrightness] = useState(100)

    useEffect(() => {
        axios.get('/api/hello')
            .then(res => console.log(res.data))
    }, [])

    const light = (what) => {
        axios.put('/0/' + what)
            .then(res => console.log(res.data))
    }

    const Dropdown = (props) => {
        return (
            <div className="dropdown">
                <button className="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton"
                        data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    {props.huone}
                </button>
                <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <button className="dropdown-item" onClick={() => setHuone('Olohuone')}>Olohuone</button>
                    <button className="dropdown-item" onClick={() => setHuone('Keittiö')}>Keittiö</button>
                    <button className="dropdown-item" onClick={() => setHuone('Makuuhuone')}>Makuuhuone</button>
                </div>
            </div>
        )
    }

    const Slider = (props) => {
        return (
            <ReactBootstrapSlider
                value={50}
                change={setBrightness(50)}
                step={1}
                max={100}
                min={0}
                orientation="vertical"
                reversed={true}
            />
        )
    }

    return(
        <div style={{display: 'flex', flexDirection: 'row'}}>
            {/*<Slider />*/}
            <div style={{display: 'flex', flexDirection: 'column'}}>
            <Dropdown huone={huone}/>
            <div style={{display: 'flex', flexDirection: 'row'}}>
            <button className="btn btn-outline-secondary btn-lg" onClick={() => light('0')}>Pois</button>
            <button className="btn btn-outline-secondary btn-lg" onClick={() => light('1')}>Päälle</button>
            <button className="btn btn-outline-secondary btn-lg" onClick={() => light('red')}>Punainen</button>
            <button className="btn btn-outline-secondary btn-lg" onClick={() => light('green')}>Vihreä</button>
            <button className="btn btn-outline-secondary btn-lg" onClick={() => light('blue')}>Sininen</button>
            <button className="btn btn-outline-secondary btn-lg" onClick={() => light('yellow')}>Keltainen</button>
            <button className="btn btn-outline-secondary btn-lg" onClick={() => light('janne')}>Janne</button>
            </div>
            </div>
        </div>
    )
};
export default App;