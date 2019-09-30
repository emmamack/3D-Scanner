//sudo chmod a+rw /dev/ttyACM0

//parameters for the user to change
float scan_resolution = 1; //in integers: best is 1, higher numbers --> lower res
int delay_time = 15;
int width = 60;
int total_height = 40;

#include <Servo.h>    //servo package
Servo h_servo;
Servo v_servo;
int h_servo_pin = 9;
int v_servo_pin = 10;
const int analog_in_pin = A0;  // Analog input pin that sensor is attached to

//initializing variables
int h_angle = 0;
int v_angle = 0;
int v_current_angle = 0;
bool keep_going = true;
int sensor_value = 0; 


void setup() { 
  delay(3000);  //delay so the human has time to run python
  h_servo.attach(h_servo_pin);
  v_servo.attach(v_servo_pin);
  Serial.begin(9600);
  goToOrigin();
}

//send sensor to origin
void goToOrigin(){
  h_servo.write(0);
  v_servo.write(0);
}

//send distance and motor positions to serial port
void sendData() {
  sensor_value = analogRead(analog_in_pin);

  Serial.print(sensor_value);
  Serial.print(",");
  Serial.print(h_angle);
  Serial.print(",");
  Serial.println(v_current_angle);
}

//move horizontal motor in clockwise direction
void moveHCW() {
  for (h_angle = 0; h_angle <= width; h_angle += scan_resolution) { // goes from 0 degrees to 180 degrees  
    // in steps of 1 degree
    h_servo.write(h_angle);              // tell servo to go to position in variable 'pos'
    delay(delay_time);                       // waits dely time for the servo to reach the position
    
    sendData();
 }
}

//move vertical motor
void moveV() {
  for (v_angle = v_current_angle; v_angle <= v_current_angle + scan_resolution -1; v_angle += 1) { // goes from current angle up height interval  
    // in steps of the resolution
    v_servo.write(v_angle);              // tell servo to go to position in variable 'pos'
    delay(delay_time);                       // waits delay time for the servo to reach the position
 }
 v_current_angle = v_angle;
}

//main loop
void loop() {
 while (keep_going == true) {   
   moveV();
   moveHCW();

   //check if end of scan has been reached
   if (v_current_angle >= total_height) {
    goToOrigin();
    break;
  }
 }
 
 //when scan is over, do nothing forever
 while(1); {}
}
