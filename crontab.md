## Resources
Crontab code assuming it is being launched from a VM:
### ***This code pulls data down once a day***
> 0 0 * * * /usr/bin/python3 /home/daniel/crontab/main.py       
> 
### ***This code pulls data down every Sunday night at 10:00pm***
> 0 22 * * SUN /usr/bin/python3 /home/daniel/crontab/main.py    
>
### ***This code pulls data down on 4/20 at 4:20am***
> 20 4 20 4 * /usr/bin/python3 /home/daniel/crontab/main.py    
>
