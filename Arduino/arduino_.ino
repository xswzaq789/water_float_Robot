#include <Servo.h>

Servo servo;

#define trig A0 //송신부
#define echo A1 //수신부
int angle = 0;

void setup(){
  servo.attach(9); 
  Serial.begin(9600);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  }
void loop()
{
  int serail_input = serial.read();
  if(serial_input == 1){
    // dc모터 on
  }
  else{
    // dc모터 off
  }
  
  long duration, distance;
  
  digitalWrite(trig, LOW);
  digitalWrite(echo, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(2);
  digitalWrite(trig, LOW);

  duration = pulseIn(echo, HIGH);
  distance = ((float)(340*duration) / 10000) /2;
  
  Serial.print("거리:");
  Serial.print(distance);
  Serial.println("cm");
  
  if(distance < 50) {
    angle = 75;
    Serial.println("장애물이 있습니다.");
    servo.write(angle);
    delay(1000);
  }
  else {
    angle = 90;
    servo.write(angle);
    delay(300);
  }

  Serial.println(angle);
  }
