#include <Servo.h>            //서보라이브러리 불러오기

Servo myServo;               // 서보객체 생성

void setup() {
  Serial.begin(9600);          //serial포트의 시리얼통신속도 지정, 데스크탑 컴퓨터와 시리얼 통신용
  Serial1.begin(9600);         // Serial1포트의 시리얼통신속도 지정, 라즈베리파이와의 통신용
  myServo.attach(8);             //digital핀 8번에 서보 제어용 핀 할당
  myServo.write(0);             // 서보모터 0도로 초기화

}

void loop() {
   int a = Serial.read(); // 라즈베리파이로 부터 serial port 내용 읽어오기 
   
   if(a == 0){
      // dc 구동 x 
   }
   else{
    //dc 모동 o
   }
   
   delay(100);
}

