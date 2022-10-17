#include <LED_BRIGHTNESS.h>

LED_BRIGHTNESS LED(3, 1); // any pin with PWM capability can be used (LED_PIN, RATE_OF_CHANGE_IE_SPEED)

void setup() {
  // put your setup code here, to run once:
}

void loop() {
  // put your main code here, to run repeatedly:
  
  for(int i=0;i<=255;i++){
    LED.make_led_brighter();
    delay(10);
  }

  
  for(int i=0;i<=255;i++){
    LED.make_led_dimmer();
    delay(10);
  }
  
  for(int i=0;i<=100;i++){
    LED.set_brightness_percent(i);
    delay(10);
  }
	
  for(int i=100;i>=0;i--){
    LED.set_brightness_percent(i);
    delay(10);
  }
	
  /*
  
	void make_led_brighter();
	void make_led_max_bright();
    	void make_led_dimmer();
    	void make_led_max_dim();
	void set_rate(int rate);
    	int set_brightness_percent(int percent);
  
  */

}
