#include <Wire.h>
#include <FaBoOLED_EROLED096.h> //для oled
#include <microDS18B20.h> //для термодатчиков
#define DS_PIN 4 // пин для термометров. первый внутри гроубокса, второй контролирует перегрев ламп

FaBoOLED_EROLED096 faboOled;

uint8_t s1_addr[] = {0x28, 0xBB, 0x20, 0x96, 0xF0, 0x1, 0x3C, 0xA5};
uint8_t s2_addr[] = {0x28, 0xC2, 0xAD, 0x48, 0xF6, 0x8E, 0x3C, 0x7E};

MicroDS18B20<DS_PIN, s1_addr> sensor1;  // Создаем термометр с адресацией
MicroDS18B20<DS_PIN, s2_addr> sensor2;  // Создаем термометр с адресацией

int flood;

void setup() {
  Serial.begin(9600);
  faboOled.begin();

  pinMode(A3, INPUT); //данные с сесора влажности почвы
  pinMode(3,OUTPUT);  //отключаемое питание сенсора влажности почвы
  pinMode(7,OUTPUT);  //реле поливочной системы (помпа)
  pinMode(8,OUTPUT);  //реле света
  pinMode(9,OUTPUT);  //зуммер
  pinMode(12,OUTPUT); //реле вентиляции (нормальный или турбо), зависит от второго термодатчика

  digitalWrite(3, LOW);
  digitalWrite(7, HIGH);
  digitalWrite(8, HIGH);
  digitalWrite(9, LOW);
  digitalWrite(12, HIGH);

}

void loop() {
  sensor1.requestTemp();      // Запрашиваем получение температуры
  sensor2.requestTemp();

  faboOled.setCursor(0, 0);
  faboOled.print(sensor1.getTemp());

  faboOled.setCursor(0,2);
  faboOled.print(sensor2.getTemp());

  digitalWrite(3,HIGH);   //запитываем датчик влажности
  delay(100);             //ждем нормальной инициализации
  flood = analogRead(A3); //читаем данные сенсора
  faboOled.setCursor(0,4);
  faboOled.print(flood);  //выводим данные
  digitalWrite(3,LOW);    //выключаем питание датчика
  Serial.println(flood);

  delay(500);
}
