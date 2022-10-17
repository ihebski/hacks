
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

#include "Arduino.h"
#include "LED_BRIGHTNESS.h"

int _pin;
int _brightness;
int _rate;

LED_BRIGHTNESS::LED_BRIGHTNESS(int pin_number, int rate)
{
	_pin = pin_number;
	_brightness = 0;


	if(rate > 255 || rate <= 0){
	  	_rate = 1;
	} else {
	  	_rate = rate;
	}
	
    init_led();
}

void LED_BRIGHTNESS::init_led()
{
    pinMode(_pin, OUTPUT);
	set_brightness();
}

void LED_BRIGHTNESS::make_led_brighter()
{
    _brightness += _rate;
	
	if(_brightness > 255){
		_brightness = 255;
	}
	
    set_brightness();
}

void LED_BRIGHTNESS::make_led_max_bright()
{
	_brightness = 255;
    set_brightness();
}

void LED_BRIGHTNESS::make_led_dimmer()
{
    _brightness -= _rate;
	
	if(_brightness < 0){
		_brightness = 0;
	}
	
    set_brightness();
}

void LED_BRIGHTNESS::make_led_max_dim()
{
    _brightness = 0;
    set_brightness(); 
}

void LED_BRIGHTNESS::set_brightness()
{		
	analogWrite(_pin, _brightness);
}

void LED_BRIGHTNESS::set_rate(int rate)
{
    if(!(rate > 255 || rate <= 0)){
	  	_rate = rate;
	}
}

int LED_BRIGHTNESS::set_brightness_percent(int percent)
{
    if(!(percent > 100 || percent < 0)){

	  	_brightness = (percent*255)/100;

	  	if(_brightness < 0){
			_brightness = 0;
		}

		if(_brightness > 255){
			_brightness = 255;
		}

	  	set_brightness();
	}

	return _brightness;
}
