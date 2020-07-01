#include <FastLED.h>
#define NUM_LEDS 5
#define DATA_PIN 6
#define BRIGHTNESS 60


CRGB leds[NUM_LEDS];

int i = 0;
int b = NUM_LEDS;

const int buttonPinRight = 2;     // the number of the pushbutton pin
int buttonStateRight = 0;         // variable for reading the pushbutton status

const int buttonPinLeft = 7;     // the number of the pushbutton pin
int buttonStateLeft = 0;         // variable for reading the pushbutton status

const int buttonPinBrake = 4;     // the number of the pushbutton pin
int buttonStateBrake = 0;         // variable for reading the pushbutton status

int starttime = 0;
int endtime = 0;

void setup() {

FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
FastLED.clear();
FastLED.show();
FastLED.setBrightness(BRIGHTNESS);

pinMode(buttonPinRight, INPUT);
pinMode(buttonPinLeft, INPUT);
pinMode(buttonPinBrake, INPUT);

}

void loop() {

buttonStateRight = digitalRead(buttonPinRight);
buttonStateLeft = digitalRead(buttonPinLeft);
buttonStateBrake = digitalRead(buttonPinBrake);

starttime = millis();
endtime = starttime;


//-------------Right Turn-----------------------
if (buttonStateRight == HIGH) {
while ((endtime - starttime) <=15000) // do this loop for up to 1000mS
{
  for(int i = 0;i<NUM_LEDS;i++){
    leds[i] = CRGB::Orange;
    FastLED.show();
    delay(150);
 }
  FastLED.clear();
  endtime = millis();
}
}

//-------------Left Turn-----------------------
if (buttonStateLeft == HIGH) {
while ((endtime - starttime) <=15000) // do this loop for up to 1000mS
{
  for(int b = 4; b <=5;b--){
    leds[b] = CRGB::Red;
    FastLED.show();
    delay(150);
 }
  FastLED.clear();
  endtime = millis();
}
}

//-------------Brake-----------------------

if (buttonStateBrake == HIGH) {
    fill_solid(leds, NUM_LEDS, CRGB::Red);
    FastLED.show();
    delay(200);
    fill_solid(leds, NUM_LEDS, CRGB::Black);
    FastLED.show();
    delay(200);
}

}
