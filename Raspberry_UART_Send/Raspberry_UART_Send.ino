int LED = 13;

void setup() {
  
  Serial.begin(115200);
  pinMode(13,OUTPUT);
}

void loop() {

  //檢查RX緩衝區，直到有資料進來
  for (int i=0;i<=99; i++) {  
    Serial.write(i);
    Serial.println(i);
    delay(1000);
  } 
  
}
