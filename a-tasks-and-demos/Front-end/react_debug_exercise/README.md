Make sure you run

### `npm i`

to install all of the dependencies

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.


## Tasks 

Pre-requisites
1) create '.env' file and paste in DEV_SOURCE_MAP_MODE='cheap-module-source-map' 
2) restart the app

Fix Bugs: 
1) Count is not displayed properly - use Dev Chrome debugger to find out why and fix it. 
2) Random Color button occassionally sets a different background color to the ones specified. Find out why and fix it. 

Test Code: 
1) Time of Day button sets background based on the "warmth of the color" and time of the day. 
This is done by calculating the temperature of the color, sorting the color and assigning cooler colors to the
morning hours and warmer colors to the end of the day. Use the debugger to change the time variable and test if the code works 
for other times. 

Stretch goal: 
1)Fix all of the console errors. 

