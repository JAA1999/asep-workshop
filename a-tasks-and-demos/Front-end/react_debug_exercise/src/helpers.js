const hexToRGB = (hex) => {
    let result = {
        red: 0,
        green: 0,
        blue: 0
    }
    
    if (hex.length === 4) {
        result.red = parseInt("0x" + hex[1] + hex[1], 16);
        result.green = parseInt("0x" + hex[2] + hex[2], 16); 
        result.blue = parseInt("0x" + hex[3] + hex[3], 16);
    } else if (hex.length === 7){
        result.red = parseInt("0x" + hex[1] + hex[2], 16);
        result.green = parseInt("0x" + hex[3] + hex[4], 16); 
        result.blue = parseInt("0x" + hex[5] + hex[6], 16);    
    }

    return result;
} 


export {hexToRGB}