
#define clockfreq 8000000 //Hz

int byteToRead[5]={0};
int count;
void setup() {
   //Initialize serial and wait for port to open:
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // prints title with ending line break
  //Serial.println("ASCII Table ~ Character Map");
 digitalWrite(13,LOW);
  count=0;

  //Timer1 Control Register
  TCCR1A=TCCR1A||0x40; //toggle 0C1A on compare match
  //DDR=XXX ///Find DDR pin of OC1A and Set it to 1.
  TCCR1B=TCCR1B||0x01 //clock frequency=
  
}


void loop() {
             

}

/* PGC manages the clock to clock data in for pic programming*/
void PGC()
{
  
}

