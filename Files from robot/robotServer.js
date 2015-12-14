
var fs = require('fs')
    net = require('net')
    child = require('child_process')

    spawn = child.spawn
    exec = child.exec

    var robot_ip = '20.10.10.115',
        robot_name = 'raspberry pi',
        robot_port = 5002

    var server_ip = '192.168.2.2',
        server_name = 'drewpi',
        server_port = 5001

    var cmd_path = __dirname + '/commands.txt'
    var motorPath = __dirname + '/text_test_1.py'
  
   fs.watch(cmd_path, {persistent:true}, function(event,fn)
   {
      if(event=='change')
      {
         var instance = spawn('python', [motorPath])
      }
   })

   var server = net.createServer(function(socket)
   {
      console.log('A client has connected.\n')
      
      socket.on('data', function(data)
      {
          console.log('I am receiving data\n')
          fs.writeFile(cmd_path, data.toString(), function(err)
          {
             if(err)
             {
                console.log(err)
             }
          })
      })
 
      socket.on('end', function()
      {
         console.log('disconnected')
      })
   });

server.listen(robot_port, robot_ip, function(){

address = server.address()

console.log('Server open at: %j\n', address)

})

