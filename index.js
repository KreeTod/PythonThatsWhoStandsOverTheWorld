const express = require("express");
const date = new Date()
let app = express();
const fs = require("fs")

const PORT = 3000 

const funny_output = JSON.parse(fs.readFileSync(__dirname + "/backend_storage/funny_output.json", "utf-8"))
const orders_json = JSON.parse(fs.readFileSync(__dirname + "/backend_storage/orders.json", "utf-8"))
// Сделать админку где будут видны все ордеры списком


app.use(express.static(__dirname + "/public"))

app.use((request, responce, next) => {
    console.log("Podklyuchenie")
    next()
})

app.get("/", (request, responce) =>{
    //responce.sendFile(__dirname + "/views/main.html");
    responce.status(228).sendFile(__dirname + "/views/main.html")
//    responce.statusMessage()
});

app.get("/order", (request, responce)=>{
    responce.status(200).sendFile(__dirname + "/views/order.html")
    console.log("some one here for order")
})

app.get("/about", (request, responce) =>{
    responce.sendFile(__dirname + "/views/inamedthisfileandwhatugonnadoaboutit.html");
})

app.get("/api/funny_text_notworking_buttons", (request, responce) =>{
    Get_fun_output();
    responce.status(200).send("Transmitting is Done");
    console.log("Worked - /api/funny_text_notworking_buttons ");
})

app.put("/api/create_an_order", (request, responce) =>{
    responce.status(200).send("Something created succsesfully");



    console.log("Imagine as if u put something in json file");
})


app.use((request, responce) =>{
    responce.sendFile(__dirname + "/views/wrongaddress.html");
})

app.listen(PORT,()=>{
    console.log(`Server is running at port ${PORT}`)
})


function CreateOrder(){
    console.log("Order has been created")
}

//написать логгер Log({уровень серъёзности: OK, WARNING, ERROR}, {описание})
//[09.03.2026 - 12:43:47.999] --- Order with index [index] has been created succsesfully.
//Тут же разные сценарии, типо не смог найти файл, не смог создать, не смог найти готовый ордер и т.д.

function Get_fun_output(){
    for (const item of funny_output){
        console.log(item.text)
    }
    return 0
}
Log(1, "Function {CreateOrder} got wrong information about phone number")
function Log(SeriosityLevel, Content){
    if (typeof(SeriosityLevel) != Int16Array && SeriosityLevel >= 0 && SeriosityLevel <= 2 ){
        console.error("Function Log was called with incorrect Seriosity Level")
    }
    if (Content === ""){
        console.error("Function Log was called with empty content")
    }
    let StringDateNTime = `[${date.getDate()}.${date.getMonth() + 1}.${date.getFullYear()} - ${date.getHours()}:${date.getMinutes()}.${date.getSeconds()}]`; 
    console.log(`${StringDateNTime} --- ${Content}`)
}