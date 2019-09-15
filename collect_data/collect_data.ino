//sudo chmod a+rw /dev/ttyACM0

#include <Servo.h>    //servo package
Servo h_servo;
Servo v_servo;
int h_servo_pin = 9;
int v_servo_pin = 10;
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to

int h_angle = 0;
int v_angle = 0;
int v_current_angle = 0;

int spd = 15;
int width = 90;
int height = 10;
int total_height = 100;

bool keep_going = true;

int sensorValue = 0; 


void setup() { 
  h_servo.attach(h_servo_pin);
  v_servo.attach(v_servo_pin);
  Serial.begin(9600);
}

void goToOrigin(){    //send sensor to origin
  h_servo.write(0);
  v_servo.write(0);
}

void move_h_cw() {    //move horizontal motor in clockwise direction
  for (h_angle = 0; h_angle <= width; h_angle += 1) { // goes from 0 degrees to 180 degrees  
    // in steps of 1 degree
    h_servo.write(h_angle);              // tell servo to go to position in variable 'pos'
    delay(spd);                       // waits 15ms for the servo to reach the position
    
    // read the analog in value:
    sensorValue = analogRead(analogInPin);
    // print the results to the Serial Monitor:
    Serial.print(sensorValue);
    Serial.println(",");
    //might need extra delay for python sending?
 }
}

void move_h_ccw() {
  for (h_angle = width; h_angle >= 0; h_angle += -1) { // goes from 0 degrees to 180 degrees  
    // in steps of 1 degree
    h_servo.write(h_angle);              // tell servo to go to position in variable 'pos'
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
}

void move_v {   //move vertical motor
  for (v_angle = v_current_angle; v_angle <= v_current_angle + height -1; v_angle += 1) { // goes from 0 degrees to 180 degrees  
    // in steps of 1 degree
    v_servo.write(v_angle);              // tell servo to go to position in variable 'pos'
    Serial.print("v_angle = ");
    Serial.println(v_angle);
    delay(spd);                       // waits 15ms for the servo to reach the position
 }
 v_current_angle = v_angle;
 Serial.println(v_current_angle);
}

void checkEnd {     //check if 

void loop() {
 while (keep_going = true) {
   move_h_cw()
   move_v()
   move_h_ccw()
   move_v()
 
 

 if (v_current_angle >= total_height) {
  Serial.println("In exit statement!");
  goToOrigin();
  break;
 }
 }
 Serial.println("Exited loop!");
 //do nothing forever
 while(1); {}
}
