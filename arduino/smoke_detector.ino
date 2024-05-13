void setup() {
  Serial.begin(9600);
}

void loop() {
  int smokeValue = analogRead(A0);
  Serial.println(smokeValue);
  delay(1000); 
}
