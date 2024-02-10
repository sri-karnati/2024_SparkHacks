# 2024_SparkHacks - Ground Analysis

A crucial part of sustainable agriculture is efficient and environmentally responsible farming. For optimal crop growth, it's essential to ensure the soil matches the
specific needs of the crop we intend to grow. However, a common challenge in modern agriculture is the overreliance on chemical fertilizers to boost crop yields. While 
these fertilizers can indeed enhance soil fertility in the short term, their excessive use leads to severe environmental repercussions, including water and soil pollution. 
Nutrient runoff from over-fertilized fields contaminates rivers, lakes, and oceans, leading to harmful algal blooms and dead zones where aquatic life cannot survive. 
Moreover, the accumulation of chemicals in the soil can degrade soil health over time, reducing its natural fertility and biodiversity.

This is where our application comes into play. By allowing users to select a crop and state from a drop-down menu, our tool aims to identify locations with the optimal soil 
composition for the chosen crop. By promoting the matching of crops to suitable soils, we can reduce the need for artificial fertilizers, thereby mitigating their 
environmental impact. Our application serves as a bridge between traditional agricultural practices and the principles of sustainable farming, encouraging the adoption of 
methods that maintain soil health, conserve water, and protect our ecosystems. Through informed decision-making, farmers can achieve high yields while also safeguarding the 
environment for future generations. 

Our tech stack consists of HTML/CSS for frontend, JavaScript and Python for frontend to backend communication, Firebase Realtime Database to store our data, and AWS
to host the application. 

We used Open-Mateo, which is a free weather forcast API (https://open-meteo.com/en/docs#hourly=). It has realtime information based on co-ordinates which we got from a 
'.csv' file (from: https://simplemaps.com/data/us-counties). With the co-ordinate data, we used the 'Soil Moisture (0-7 cm)' and 'Precipitation (rain + snow)' from each county over a year that we averaged out for a more reliable result.

By setting hypothetical conditions for each fruit and vegetable, of which we calculate which county is the best at cultivating it, we display it in Ascending order. 

The conditions are as follows:
Corn:
 Ideal Soil Moisture: 0.23 (23%)
 Ideal Precipitation: 20 mm/day
Potatoes:
 Ideal Soil Moisture: 0.2 (20%)
 Ideal Precipitation: 25 mm/day
Wheat:
 Ideal Soil Moisture: 0.12 (12%)
 Ideal Precipitation: 15 mm/day
Strawberries:
 Ideal Soil Moisture: 0.25 (25%)
 Ideal Precipitation: 30 mm/day
Tomatoes:
 Ideal Soil Moisture: 0.18 (18%)
 Ideal Precipitation: 35 mm/day
Cucumbers:
 Ideal Soil Moisture: 0.3 (30%)
 Ideal Precipitation: 40 mm/day
Onions:
 Ideal Soil Moisture: 0.15 (15%)
 Ideal Precipitation: 10 mm/day
