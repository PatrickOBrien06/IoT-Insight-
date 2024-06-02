# IoT-Insight

This is an IoT manager project I made where a programmable microcontroller is able to connect to a server and send live information directly to the user, VIA websockets. 

I decided to go for a more expandable design where users can authenicate their sensor in the database, matching with the ID the sensor sends in an HTTP request. Whenever the sensor accesses "/data" and sends a request it will follow these rules.

- Server checks if the attribute "sensor_id" of the HTTP request is matching the Sensor table
- If True save the data from the HTTP into the SensorData table
- If False just exit the root


