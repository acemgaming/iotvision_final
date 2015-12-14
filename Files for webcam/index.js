var express = require('express')
	app = require('express')(),
    http = require('http').Server(app),
	io = require('socket.io')(http)
	child = require('child_process')
	fs = require('fs')
	
	
	spawn = child.spawn
	exec = child.exec
	
	var server_port = 5000
	
	var video_genPath = __dirname + '/videotest.py'
	var image_genPath = __dirname + '/image_capture.py'
	var img_loc = __dirname + '/public/images/testimg.png'
	var sockets = {}
	
	app.use(express.static('public'))
	
	//app.get(path, callback [, callback ...])
	//Routes HTTP GET requests to the specified path with the specified callback functions.
	app.get('/', function(req, res){
		
		//res.send('yeah bebe')
		res.sendFile(__dirname + '/index.html')
	})
	
	//app.get('/about', function(req,res)
	//{
	//	res.sendFile(__dirname + test.html);
	//})
	
	//Update the web page image
	function updateImg(io)
	{
		io.sockets.emit('update_img', '/images/testimg.png?_t='+(Math.random()*100000))
	}
	
	//When a user connects
	io.on('connection', function(socket)
	{
		//allows for more than one connection
		sockets[socket.id] = socket
		
		console.log('connection established')
		
		//Check to see when the image file changes
		fs.watch(img_loc, {persistent: true}, function(event, fileName)
		{
			//console.log("event is: " + event)
			
			if(event == 'change')
			{
				//console.log("I changed!")
				
				updateImg(io)
			}
		})
		
		//When a user disconnects
		socket.on('disconnect', function(){
			console.log('user disconnected')
			delete sockets[socket.id]
		})
		
	})
	
	//Listen for requests
	http.listen(server_port,function(){
		
		//var host = server.address().address
		//var port = server.address().port
		
		console.log('listening on port: ' + server_port.toString())
	})