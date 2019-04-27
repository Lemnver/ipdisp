#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
String sentString = "";
char data;
void setup(){
  Serial.begin(9600);
  
  lcd.begin(16,2);
  lcd.setCursor(0, 0);
  lcd.print("waiting");
  lcd.setCursor(0, 0);

}
void loop(){
  if (Serial.available() > 0) {
    lcd.clear();
    lcd.print("reading");
    char c = Serial.read();
    Serial.write(c);
    sentString += c;
    if (c == 'e'){
      lcd.clear();
      lcd.print(sentString);
      sentString == "";
    }
  }
  Serial.write("ping\n");
  
}


