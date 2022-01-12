import { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import BackGroundColorChooser from './BackgroundColorChooser';
import TopClicksDisplay from './TopClicksDisplay'


function App() {

  const colors =  ['#fe7c00', '#ffd832', '#00b4ab', '#0269a4', '#022b56'];
  const [bgColor, setBgColor] = useState('#022b56');
  const [colorClicks, setColorClicks] = useState({});

  return (
    <div className="App" >
      <header 
        className="App-header"
        style={{"background": bgColor }}
      >
        
        <img src={logo} className="App-logo" alt="logo" />
        <h1>{bgColor}</h1>
        <BackGroundColorChooser
          setColor={setBgColor}
          colors={colors} 
          colorClicks={colorClicks}
          setColorClicks={setColorClicks}
        />
        <TopClicksDisplay 
          clicks = {colorClicks}
        />
      </header>
    </div>
  );
}

export default App;
