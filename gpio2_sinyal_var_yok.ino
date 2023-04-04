// HIGH olduktan sonra sinyali kessen bile HIGH'ta kalıyor GND'ye deyince LOW'a düşüyor.
// Denemek lazım
// GPIO2 sadece GND'ye dokununca yok'a düşüyor onun dışında hep var
// GPIO12 sinyal gelince (3V da oluyor gerilim bölücüyle çalıştı) var yokken yok. Sorunsuz çalışıyor gibi 
void setup() {
  // GPIO2 pinini giriş olarak ayarla
  pinMode(12, INPUT);
  
  // Seri haberleşme hızını ayarla
  Serial.begin(115200);
}

void loop() {
  // GPIO2 pinindeki sinyal durumunu oku
  int pinValue = digitalRead(12);
  
  // Sinyal durumunu seri monitöre yazdır
  if (pinValue == HIGH) {
    Serial.println("GPIO2 piminde sinyal var.");
  } else {
    Serial.println("GPIO2 piminde sinyal yok.");
  }
  
  // Kısa bir gecikme ekle
  delay(1000);
}
