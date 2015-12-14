/*webcamServer.js
*
*Author: James Massey
*Date Created: 11/18/2015
*
*
*Brief:  This program will check for when a command text file changes 
*        and send those commands to the robot.
*/  

var fs = require('fs'),
    net = require('net')

var webcam_ip = '192.168.2.4',
    webcam_name = 'raspberrypi',
    webcam_port = 5000

var server_ip = '192.168.2.2',
    server_name = 'drewpi',
    server_port = 5001


var cmd_file = __dirname + '/commands.txt'

var webcam_client = net.connect(server_port, server_ip, function(){

   console.log('I have connected to the server\n')
   console.log('Awaiting changes to: ' + cmd_file)

   fs.watch(cmd_file, {persistent: true}, function(event, fn)
   {
      if(event == 'change')
      {
         fs.readFile(cmd_file, 'utf8', function(err,data)
         {
            webcam_client.write(data)
         });
      }
   });

});
