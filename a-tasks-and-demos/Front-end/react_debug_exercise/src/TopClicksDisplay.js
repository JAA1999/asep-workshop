import React from 'react';


const TopClicksDisplay = (props) => {
    const {clicks} = props;

    const clickEntries = clicks ? Object.entries(clicks) : [];

    
    return(
        <div className="top-clicks-container">
            {/* {{clicks}} */}
            {clicks && clickEntries.sort((a,b)=>a[1] - b[1]).map(ent =>
                <li>{ent[0]}: {ent[1]}</li>
            )}
        </div>
    )
}


export default TopClicksDisplay;