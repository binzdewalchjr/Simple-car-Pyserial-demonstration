int MotorSpeed;
int Drive;
int Distance2WallRaw;
float Distance2WallMeter;
long LoopTime
unsigned long timer = 0;
bool initLoopTime = false;
bool StopProgram = false;
#include <Wire.h>
//#include <HCSR04.h>
#define LeftMotor 3
#define RightMotor 5
#define SonicTrigger
#define SonicEcho
//HCSR04 SonicSensor(2,4); // (trig pin, echo pin)
  // SonicSensor.distance() is the current distnace
#define SonicTrigger 
#define SonicEcho 
void setup() {
  Wire.begin();
  Serial.begin(9600);
  pinMode(SonicTrigger,OUTPUT);
  pinMode(SonicEcho,INPUT);
  pinMode(LeftMotor,OUTPUT);
  pinMode(RightMotor,OUTPUT);
  timer = micros()

}

void loop() {
  if(Serial.available() > 0{
    String serString = Serial.readStringUntil('\n');
    PCRead(serString);
  }
  if (initLoopTime && !StopProgram){
    SyncTime(LoopTime);
    unsigned long CurrentTime = micros();

    //Send Read data over to PC
    sendToPC(&CurrentTime);
    sendToPC(&DistanceToWall);
    
  }
}
void SyncTime(unsigned long deltaT)
{
  unsigned long TimeNow = micros();
  long 
}

void sendToPC(int* data)
{
  byte* byteData = (byte*)(data);
  Serial.write(byteData, 2);
}
void sendToPC(float* data)
{
  byte* byteData = (byte*)(data);
  Serial.write(byteData, 4);
}
 
void sendToPC(double* data)
{
  byte* byteData = (byte*)(data);
  Serial.write(byteData, 4);
}

void sendToPC(unsigned long* data)
{
  byte* byteData = (byte*)(data);
  Serial.write(byteData, 4);
}
