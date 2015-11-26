/*serverCommand.js
 * 
 * Author: James Massey
 * Date Created: 11/17/2015
 * Date Revised: 11/17/2015
 * Brief: This script will serve as the central control unit.
 * 
*/

var fs = require('fs')
	net = require('net')
	
var server_ip = '192.168.2.2',
	server_name = 'drewpi',
	server_port = 5001
	
var robot_ip = '192.168.2.3',
	robot_name = 'raspberrypi',
	robot_port = 5002
	
var webcam_ip = '192.168.2.4',
	webcam_name = 'raspberrypi',
	webcam_port = 5000
	
var cmd_path = __dirname + '/command.txt'


// client   //
var robot = net.connect(robot_port, robot_ip, function()
{
   console.log('I have connected to the robot')
  
   robot.on('data', function()
   {
      console.log('I have received data from the robot')
   })
})

//   server   //
var server = net.createServer(function(socket)
{
   console.log('A client has connected\n')   

   socket.on('data', function(data)
   {
      //console.log('I received data from the webcam\n')
      robot.write(data)  
   })

   socket.on('end', function()
   {
      console.log('A client has disconnected')
   })
})

server.listen(server_port, server_ip, function(){

address = server.address()

console.log('Main server open at: %j\n', address)

})


