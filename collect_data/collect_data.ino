//servo package

#include <Servo.h>
Servo h_Servo;
Servo v_Servo;
int h_servo_pin = 9;
int v_servo_pin = 10;
int h_angle = 0;
int v_angle = 0;
int v_current_angle = 0;
int spd = 15;
int dir = 1;
int width = 90;
int height = 10;
int total_height = 100;
bool keep_going = true;
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
int sensorValue = 0;        // value read from the pot


void setup() {
  
  //pinMode(motor, OUTPUT);  
  h_Servo.attach(h_servo_pin);
  v_Servo.attach(v_servo_pin);
  Serial.begin(9600);
}

void goToOrigin(){ //send sensor to origin
  h_angle = 0;
  v_angle = 360;
  h_Servo.write(h_angle);
  v_Servo.write(v_angle);
}

void loop() {
 while (keep_going = true) {
 //move horizontal motor one direction
 for (h_angle = 0; h_angle <= width; h_angle += dir) { // goes from 0 degrees to 180 degrees  
    // in steps of 1 degree
    h_Servo.write(h_angle);              // tell servo to go to position in variable 'pos'
    delay(spd);                       // waits 15ms for the servo to reach the position
    
    // read the analog in value:
    sensorValue = analogRead(analogInPin);
    // print the results to the Serial Monitor:
    Serial.print(sensorValue);
    Serial.println(",");
    //might need extra delay for python sending?

 }
 dir = dir * (-1);

 //move vertical motor in one direction
 for (v_angle = v_current_angle; v_angle <= v_current_angle + height -1; v_angle += 1) { // goes from 0 degrees to 180 degrees  
    // in steps of 1 degree
    v_Servo.write(v_angle);              // tell servo to go to position in variable 'pos'
    Serial.print("v_angle = ");
    Serial.println(v_angle);
    delay(spd);                       // waits 15ms for the servo to reach the position
 }
 v_current_angle = v_angle;
 Serial.println(v_current_angle);


 //move horizontal motor back
 for (h_angle = width; h_angle >= 0; h_angle += dir) { // goes from 0 degrees to 180 degrees  
    // in steps of 1 degree
    h_Servo.write(h_angle);              // tell servo to go to position in variable 'pos'
    delay(spd);                       // waits 15ms for the servo to reach the position
    
    // read the analog in value:
    sensorValue = analogRead(analogInPin);
    // print the results to the Serial Monitor:
    Serial.print(sensorValue);
    Serial.print(",");
    Serial.print(h_angle);
    Serial.print(",");
    Serial.print(v_current_angle);
    Serial.println(",");
    //might need extra delay for python sending?
 }
 dir = dir * (-1);

 //move vertical motor in same direction
 for (v_angle = v_current_angle; v_angle <= v_current_angle + height -1; v_angle += 1) { // goes from 0 degrees to 180 degrees  
    // in steps of 1 degree
    v_Servo.write(v_angle);              // tell servo to go to position in variable 'pos'
    Serial.print("v_angle = ");
    Serial.println(v_angle);
    delay(spd);                       // waits 15ms for the servo to reach the position
 }
 v_current_angle = v_angle;
 Serial.println(v_current_angle);

 if (v_current_angle >= total_height) {
  Serial.println("In exit statement!");
  keep_going = false;
  break;
 }
 }
 Serial.println("Exited loop!");
 //do nothing forever
 while(1); {}
}

//h_angle + width*dir
