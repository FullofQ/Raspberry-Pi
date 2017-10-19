int i=0;
void setup() {
  Serial.begin(115200);
}
void loop() {
  if (Serial.available() > 0) {
    i=Serial.read();
    Serial.write(i); 
  }
}
