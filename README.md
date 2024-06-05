# IoT-Insight

This is an IoT manager project I made where a programmable microcontroller is able to connect to a server and send live information directly to the user, VIA websockets. 

I decided to go for a more expandable design where users can authenicate their sensor in the database, matching with the ID the sensor sends in an HTTP request. Whenever the sensor accesses "/data" and sends a request it will follow these rules.

- Server checks if the attribute "sensor_id" of the HTTP request is matching the a value in the Sensor table
- If True save the data from the HTTP into the SensorData table
- If False just exit the root

While developing this I found that there was a large security flaw where someone can construct their own HTTP request to the server and guess what the ID of a sensor is until they find it then they could pretend to be that sensor and send false information to the server.

I could get around this by using larger, harder to guess IDs while also creating time limits on "/data" and encrypting the sensor ID.

 
