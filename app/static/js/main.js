
setInterval(function loa(){

        var load = document.getElementById("loading");


            load.style.display="none";

        },3000);


        setInterval(function ()
        {

            var Currentime = new Date();
            var hour = Currentime.getHours();
            var minute = Currentime.getMinutes();
            var second = Currentime.getSeconds();

            if(hour >=24){
                hour = hour - 24;
            }

            if(hour < 10){

                hour = "0" + hour;
            }

            if(minute < 10) {

                minute = "0" + minute;
            }

                if(second < 10){
                    second = "0" + second;
                }



            var myclock = hour +":"+ minute + ":"+ second;
            document.getElementById("h").innerText=myclock;

        },1000);