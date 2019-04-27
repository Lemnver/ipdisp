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
    char c = Serial.read();
    sentString += c;
    if (sentString.length() == 15){
      lcd.clear();
      lcd.print(sentString);
      sentString == "";
    }
  }
  Serial.write("ping\n");
  
}


