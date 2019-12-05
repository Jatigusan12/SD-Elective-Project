client = mqtt.connect("wss://test.mosquitto.org:8081/mqtt")
client.subscribe("Emergency")
client.subscribe("EatingTime")


client.on('connect', function () {
  console.log("Connected Succesfully")
})

emergency = () =>{
  client.publish("Emergency");
  client.on("message", function (topic, payload) {
    var payload="Emergency Alarm";
    console.log("Received { topic:"+topic+"; payload: "+payload+" }" )
    if (topic == "Emergency") {
      document.getElementById("block1").innerHTML = payload;
      document.getElementById("block2").innerHTML = payload;
    }
  })
  client.subscribe({
    'Emergency': { qos: 0 }
  })
};

eatingTime = () =>{
  client.publish("EatingTime");
  client.on("message", function (topic, payload) {
    var payload="Eating Time Alarm"
    console.log("Received { topic:"+topic+"; payload: "+payload+" }" )
    if (topic == "EatingTime") {
      document.getElementById("block1").innerHTML = payload;
      document.getElementById("block2").innerHTML = payload;
    }
  })
  client.subscribe({
    'EatingTime': { qos: 0 }})
};

goingToUSC = () =>{
  client.on("message", function (topic, payload) {
    var payload="Going To USC Alarm"
    console.log("Received { topic:"+topic+"; payload: "+payload+" }" )
    if (topic == "EatingTime") {
      document.getElementById("status").innerHTML = payload;
    }
  })
  client.subscribe({
    'GoingToUSC': { qos: 0 }})
};


pagingForSomeone = () =>{
  client.on("message", function (topic, payload) {
    var payload="Paging for Someone Alarm"
    console.log("Received { topic:"+topic+"; payload: "+payload+" }" )
    if (topic == "EatingTime") {
      document.getElementById("status").innerHTML = payload;
    }
  })
  client.subscribe({
    'GoingToUSC': { qos: 0 }})
};



// client.on("message", function (topic, payload) {
//   console.log("Received { topic:"+topic+"; payload: "+payload+" }" )
//   if (topic == "Emergency") {
//     document.getElementById("status").innerHTML = payload;
//     console.log(payload)
//   }
// })


client.subscribe({
  'Emergency': { qos: 0 },
  'EatingTime': { qos: 0 },
  'GoingToUSC': { qos: 0 },
  'Paging': { qos: 0 },
  'Off': { qos: 0 },
})

