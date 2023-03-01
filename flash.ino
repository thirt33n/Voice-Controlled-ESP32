void setup() {
  pinMode(2, OUTPUT);
  Serial.begin(115200);
}
void loop() {
  if (Serial.available() > 0) {
    int state = Serial.read();
    if (state == 53) {
      digitalWrite(2, HIGH);
      Serial.println("LED SWITCHED ON");
    }
    if (state == 54 ) {
      digitalWrite(2, LOW);
      Serial.println("LED SWITCHED OFF");
    }
  }
  delay(50);
}