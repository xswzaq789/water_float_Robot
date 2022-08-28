
#define ENABLE_A 3
#define IN1 4
#define IN2 5

byte speedDC = 255;

void setup(){
  Serial.begin(9600);
  pinMode(ENABLE_A, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
}


void loop(){
  digitalWrite(IN1,HIGH);  
  digitalWrite(IN2,LOW);
  analogWrite(ENABLE_A, 50);
  delay(3000);
}
