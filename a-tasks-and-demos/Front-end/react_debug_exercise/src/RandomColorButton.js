import React, {useState, useEffect} from 'react';



const RandomColorButton = (props) => {
    const {colors, setColor, className} = props;
    const [btnColor, setBtnColor] = useState(colors[0])
    const selectRandomColor = () => {
        return colors[Math.floor(Math.random()*colors.length + 1)]
    }
    useEffect(() => {
        let myInterval = setInterval(() => {
            setBtnColor(selectRandomColor())
        }, 1000)
        return ()=> {
            clearInterval(myInterval);
        };
    });



    return(
        <button 
            onClick={() => setColor(selectRandomColor())} 
            style={{background:btnColor}}
            className={className}    
        >
            Random Color    
        </button>
    )
}


export default RandomColorButton;