var app = require('express')(),
	http = require('http').Server(app),
	io = require('socket.io')(http),
	child = require('child_process')
	fs = require('fs')
	
	spawn = child.spawn
	exec = child.exec
	
var PORT = 3000

var testPath = __dirname + '/Test.py'
//var motorPath = __dirname + '/GPIO_Control.py'
var cmdPath = __dirname + '/commands.txt'

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html')
})

io.on('connection', function(socket)
{
	console.log('connection established: '+  socket.handshake.address.port)
	
	socket.on('message', function(message)
	{
		console.log('I got clicked')
	})
	
	//When the forward button is pressed
	socket.on('Forward', function(){
		console.log("I am moving forward!")
                fs.writeFile(cmdPath, 'Forward', function(){
           		console.log("I wrote to file")
		})
        })
	
        //When the back button is pressed
	socket.on('Back', function(){
		console.log("I am moving back!")
                fs.writeFile(cmdPath, 'Backward', function(){
			console.log("I wrote to file")
		})
        })

        //When the right button is pressed
	socket.on('Right', function(){
		console.log("I am moving to the right!")
                fs.writeFile(cmdPath, 'Right', function(){
			console.log("I wrote to file")
             })
	})

        //When the left button is pressed
	socket.on('Left', function(){
		console.log("I am moving to the left!")
                fs.writeFile(cmdPath, 'Left', function(){
			console.log("I wrote to file")
             }) 
	})

        //When a client disconnects.
	socket.on('disconnect', function()
	{
		console.log('user disconnected')
		//exit()
	})	
})

http.listen(PORT, function(){
  console.log('listening on port: ' + PORT.toString())
})
