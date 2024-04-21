#include <Arduino.h>

String inputString = ""; // a string to hold incoming data
double rangeValue = 0.0;

void setup() {
  Serial.begin(9600); // initialize serial communication
}

void loop() {
  // Check if there is data available to read from serial
  if (Serial.available() > 0) {
    char incomingChar = Serial.read(); // read the incoming byte

    // If the received character is a newline, process the received message
    if (incomingChar == '\n') {
      // Convert the received string to a double value
      rangeValue = inputString.toDouble();
      // Clear the string for the next message
      inputString = "";
    } else {
      inputString += incomingChar; // Append the received character to the input string
    }
  }

  // Check the range value published by ROS 2
  if (rangeValue > 0.0) {
    // If range value is greater than 0, motion is detected, rotate the motor for one rotation
    rotateMotorOnce();
    // Reset the range value
    rangeValue = 0.0;
  }
}

void rotateMotorOnce() {
  // Set motor control pins
  int motorPin1 = 9;  // Example motor control pin 1
  int motorPin2 = 10; // Example motor control pin 2

  // Set motor speed and direction for one rotation
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);

  // Adjust delay based on your motor and desired rotation speed
  delay(1000);  // Adjust the delay to achieve one rotation

  // Stop the motor
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
}
