import React from "react";
import RandomColorButton from "./RandomColorButton";
import ct from 'color-temperature';
import { hexToRGB } from './helpers'

const BackGroundColorChooser = (props) => {
    const {colors, setColor, colorClicks, setColorClicks} = props;

    const sortColorsByTemperature = () => {
        return colors.sort( (a,b) => ct.rgb2colorTemperature(hexToRGB(a)) - ct.rgb2colorTemperature(hexToRGB(b)) )
    }

    const handleClick = (color) => {
        setColor(color);
        setColorClicks({
            ...colorClicks, 
            [color]: colorClicks[color] ? colorClicks[color] + 1 : 1
        });
    }
        

    const getPartOfDayIndex = () =>{
        let today = new Date();
        let currentHour = today.getHours(); 
        let res = Math.floor(currentHour/(24/colors.length));

        return res;
    }
    
    const getTimeOfDayColor = () => {
        const sorted_colors = sortColorsByTemperature();
        return sorted_colors[getPartOfDayIndex()];
    }
    
    return (
        <div className="color-chooser">
            {
                colors && colors.map(color => {
                    return(
                        <button
                            onClick={()=> handleClick(color)} 
                            style={{background: color}}
                        >
                            {color}
                        </button>
                    )
                })
            }
            <RandomColorButton
                colors={colors}
                setColor={setColor}
            />

            <button onClick={()=>handleClick(getTimeOfDayColor())}>Time Of Day Color</button>
        </div>  
    );

}


export default BackGroundColorChooser;