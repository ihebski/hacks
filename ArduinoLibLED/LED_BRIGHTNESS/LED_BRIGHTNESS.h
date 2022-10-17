
/*
  LED_BRIGHTNESS.h - Library for controlling LED brightness.
  Released into the public domain.
  
  Created by Jahanzaib Khan Durrani, April 14, 2017.
  Copyrights@OffS3c All Rights Reserved.
  https://github.com/OffS3c
  https://facebook.com/OffS3c
  https://twitter.com/OffS3c
  https://linkedin.com/in/OffS3c
*/

#ifndef LED_BRIGHTNESS_h
#define LED_BRIGHTNESS_h

#include "Arduino.h"

class LED_BRIGHTNESS
{
  public:
    LED_BRIGHTNESS(int pin_number, int rate);
    void make_led_brighter();
	void make_led_max_bright();
    void make_led_dimmer();
    void make_led_max_dim();
	void set_rate(int rate);
    int set_brightness_percent(int percent);
  private:
    int _pin;
    int _brightness;
    int _rate;
	void init_led();
	void set_brightness();
};

#endif