// Copy this code and enter into the Arduino IDE after installing ESP8266WiFi and ESP8266HTTPClient after then uncommect this code

// #include <ESP8266WiFi.h>
// #include <ESP8266HTTPClient.h>

// const char* ssid = "<SSID>";
// const char* password = "<PASSWORD>";
// const char* serverHost = "<SERVER_IP_ADDRESS>";

// WiFiClient client;

// void setup() {
//     Serial.begin(115200);
//     WiFi.begin(ssid, password);

//     while (WiFi.status() != WL_CONNECTED) {
//         delay(1000);
//         Serial.println("Connecting to WiFi...");
//     }
//     Serial.println("Connected to WiFi");
// }

// void loop() {
//     if (WiFi.status() == WL_CONNECTED) {
//         HTTPClient http;
//         http.begin(client, String(serverHost) + "/data"); // Specify the URL

//         http.addHeader("Content-Type", "application/json"); // Specify content-type header
//         String postData = "{\"data\":\"Sensor data or any other data\"}";

//         int httpResponseCode = http.POST(postData); // Send the request

//         if (httpResponseCode > 0) {
//             String response = http.getString(); // Get the response to the request
//             Serial.println(httpResponseCode); // Print return code
//             Serial.println(response); // Print request answer
//         } else {
//             Serial.print("Error on sending POST: ");
//             Serial.println(httpResponseCode);
//         }

//         http.end(); // Free resources
//     }

//     delay(1000); // Send a request every second
// }
