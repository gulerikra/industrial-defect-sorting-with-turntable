// GPIO12 sinyal gelince var, yokken yok. Sorunsuz çalışıyor gibi. Bunu direk olc y0 üzerinden okuyarak yaptım. 

// YAPILACAKALR
// Genel konvo kodunda da denemek lazım. 
// Sinyali al ve saat ile birlikte http isteğine yazdır(Motor çalışıyor/durdu gibi).
// Resim çek ve gönder.

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
