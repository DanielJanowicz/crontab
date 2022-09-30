## Crontab code assuming it is being launched from a VM:
### ***This code pulls data down once a day***
> 0 0 * * * /usr/bin/python3 /home/daniel/crontab/main.py       
> 
### ***This code pulls data down every Sunday night at 10:00pm***
> 0 22 * * SUN /usr/bin/python3 /home/daniel/crontab/main.py    
>
### ***This code pulls data down at 11:30am on the first day of the month, every quarter***
> 30 11 1 */3 * /usr/bin/python3 /home/daniel/crontab/main.py    
>
