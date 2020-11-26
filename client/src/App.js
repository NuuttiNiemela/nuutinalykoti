import React, { useState, useEffect } from 'react'
import axios from 'axios';
import ReactBootstrapSlider from 'react-bootstrap-slider';

const App = props => {
    const [huone, setHuone] = useState('Olohuone')
    const [brightness, setBrightness] = useState(100)
    const [power, setPower] = useState('0')
    const [color, setColor] = useState('joo')

    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    useEffect(() => {
        axios.get('/api/hello')
            .then(res => console.log(res.data))
    }, [])

    const light = (what) => {
        axios.get('/0/' + what)
            .then(res => setPower(res.data.power))
//            .then(res => setColor(res.data.color))
            .then(() => console.log(power))
            .then(() => console.log(color))
            .then(() => console.log(brightness))
    }

    const lightAndBrightness = (color, brightness) => {
//            Brightness 1-254
            axios.get('/0/lights/' + color + '/' + brightness)
                .then(res => console.log(res.data))
    }

    const lightAndBrightnessXY = (xColor, yColor, brightness) => {
//         Brightness 1-254
//         XY-colors 0-65535
        axios.get('/0/lightsxy/' + xColor + '/' + yColor + '/' + brightness)
            .then(res => console.log(res.data))
    }

    const disco = async (pulse) => {
        let x = '1'
        let y = '65535'
        let br = '254'

        for (let a = 0; a < 6; a++) {
            if (parseInt(x) > 65535) x = '65535'
            if (parseInt(x) < 0) x = '0'
            if (parseInt(y) > 65535) y = '65535'
            if (parseInt(y) < 0) y = '0'
            if (parseInt(br) > 254) br = '254'
            if (parseInt(br) < 1) br = '1'

            console.log('a: ' + a)
            console.log('x: ' + x)
            console.log('y: ' + y)
            console.log('br: ' + br)
            lightAndBrightnessXY(x, y, br)
            await sleep(pulse)
            x = (parseInt(x) + 13107).toString()
            y = (parseInt(y) - 13107).toString()
        }
    }


    const discoHex = async (pulse, times) => {
        const colors = [ "4a418a",
            "8f2686",
            "dc4b31",
            "da5d41",
            "6c83ba",
            "d9337c",
            "e57345",
            "e78834",
            "a9d62b",
            "ebb63e",
            "c984bb",
            "d6e44b",
            "e491af",
            "efd275",
            "e8bedd",
            "f1e0b5",
            "f2eccf",
            "dcf0f8",
            "eaf6fb",
            "f5faf6" ]

        for (let a = 0; a < times; a++) {
            for (let color of colors) {
                console.log('Väri: ' + color + 'ja a: ' + a)
                lightAndBrightness(color, '254')
                await sleep(pulse)
            }
        }


    }


    const ColorInput = (props) => {
        return (
            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text" id="inputGroup-sizing-default">Väri</span>
              </div>
              <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"/>
            </div>
        )
    }

    const BrightnessInput = (props) => {
            return (
                <div class="input-group mb-3">
                  <div class="input-group-prepend">
                    <span class="input-group-text" id="inputGroup-sizing-default">Kirkkaus</span>
                  </div>
                  <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"/>
                </div>
            )
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
                <button className="btn btn-outline-secondary btn-lg" onClick={() => lightAndBrightness('f5faf6', '127')}>Väri</button>
                <button className="btn btn-outline-secondary btn-lg" onClick={() => lightAndBrightnessXY('1', '65000', '254')}>VäriXY</button>
                <button className="btn btn-outline-secondary btn-lg" onClick={() => discoHex('200', 2)}>Disco</button>
            </div>
                <ColorInput/>
                <BrightnessInput/>
            </div>
        </div>
    )
};
export default App;