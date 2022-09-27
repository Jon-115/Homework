// 1 Ensure that GET requests do not have a body, if so handle appropriately
// 2 Ensure PUT requests take parameters through the path

// 3 Delete requests should not have a body
// 4 Part II: Using ejs, display your todo list in the browser

const express = require('express')
const app = express()
app.use(express.json())

const ejs = require('ejs')
app.set('view engine', 'ejs')

const logger = require('./logs.js')        // linking files
let todoList = require('./database.js')

app.all('*', (req, res, next) => {
    logger.info({
        action: req.method,
        path: req.path,
        body: req.body,
        time: new Date()
    })
    next()
})


// let todoList = [{ 'task' : "wash car", 'prio' : "low"},{ "task" : "do dishes", "prio" : "medium"}, { 'task' : "doctor's appointment", "prio": "high"} ]
//----------------------------------------------------------------------------------------------
app.get('/list', function (req, res) {
    res.render("todoList", { todoList: todoList})
})

app.get('/todolist/:prio'), function (req, res) {
    let priority = req.param.prio
    for (let i = 0; todoList.length; i++) {
        if (todoList[i].prio == priority) {
            res.send(todoList[i])
        }
    }
}

app.get('/todoList/:task', (req, res, next) => {

    if (Object.keys(req.body).length != 0) {
        res.statusCode = 400
        res.send(`Call contains a body.`)
    }
    else{
        let taskName = req.params.task
        let over = false
        for (let i = 0; i < todoList.length; i++) {
            if (todoList[i].task == taskName) {
                res.send(todoList[i])
                over = true
            }
        } 
    
        if(over == false) {
        logger.error({
            message: 'task is not on list',
            action: req.method,
            path: req.path,
            body: req.body,
            time: new Date()
        })
        next()
        res.statusCode = 400
        res.send(`The task ${taskName} is not on the To-do List`)
        }
    }
})

app.get('/todoList', (req,res) => {

    if (Object.keys(req.body).length != 0) {
        res.statusCode = 400
        res.send(`Call contains a body.`)
    }
    else{
    res.send(todoList)
    }
})
//----------------------------------------------------------------------------------------------
app.post('/todoList', (req,res, next) => {
    console.log(req.body)
    let task = req.body.task
    let prio = req.body.prio

    if(task.length > 20){    // Max character limit
        logger.error({
            level: 'error',
            message: 'task is too long',
            action: req.method,
            path: req.path,
            body: req.body,
            time: new Date()
        })
        next()
        res.statusCode = 400
        res.send('Tasks name is too long')
    }
    else if(typeof(task) != 'string' || typeof(prio) != "string") { // Checks type of paramters
        logger.error({
            message: 'task is of incorrect type',
            action: req.method,
            path: req.path,
            body: req.body,
            time: new Date()
        })
        next()
        res.statusCode = 400
        res.send('Incorect type')
    }
    else if(prio != "low" && prio != "medium" && prio != "high") { // Checks for correct prio
        logger.error({
            message: 'incorrect priority',
            action: req.method,
            path: req.path,
            body: req.body,
            time: new Date()
        })
        next()
        res.statusCode = 400
        res.send('Incorrect priority')
    }
    else { 
        lastIndex = todoList[len(todoList)-1]
        id = lastIndex['id']
        newtodoListItem = {"task": task, "prio": prio, "id": id + 1}
        todoList.push(newtodoListItem)
        res.send(newtodoListItem);
    }
})
//----------------------------------------------------------------------------------------------
app.put('/todoList/:task/:prio', (req, res ,next) => {
    let task = req.params.task
    let prio = req.params.prio
    let over = false
    
    if(task.length > 20){    // Max character limit
        logger.error({
            message: 'task is too long',
            action: req.method,
            path: req.path,
            body: req.body,
            time: new Date()
        })
        next()
        res.statusCode = 400
        res.send('Tasks name is too long')
    }
    else if(typeof(task) != 'string' || typeof(prio) != "string") { // Checks type of paramters
        logger.error({
            message: 'task is of incorrect type',
            action: req.method,
            path: req.path,
            body: req.body,
            time: new Date()
        })
        next()
        res.statusCode = 400
        res.send('Incorect type')
    }
    else if(prio != "low" && prio != "medium" && prio != "high") { // Checks for correct prio
        logger.error({
            message: 'invalid priority',
            action: req.method,
            path: req.path,
            body: req.body,
            time: new Date()
        })
        next()
        res.statusCode = 400
        res.send('Incorrect priority')
    }
    else if(prio == "low" || prio == "medium" || prio == "high"){
        for (let i = 0; i < todoList.length; i++){
            if (task == todoList[i].task){
                todoList[i] = {'task': task, 'prio': prio}
                res.send(todoList[i])
                over = true
            }
        }
        if(over == false) {
            logger.error({
                message: 'task is not on list',
                action: req.method,
                path: req.path,
                body: req.body,
                time: new Date()
            })
            next()
        res.statusCode = 400   
        res.send('Task does not exist')
        }
    }
})
//----------------------------------------------------------------------------------------------
app.delete('/todoList/:task', (req, res, next) => {
    let taskName = req.params.task
    let over = false


    if (Object.keys(req.body).length != 0) {
        res.statusCode = 400
        res.send(`Call contains a body.`)
    }
    else{
        for (let i = 0; i < todoList.length; i++) {
            if (todoList[i].task == taskName) {
                let deleted = todoList[i]
                todoList.splice(i, 1)
                res.send(deleted)
                over = true
            }
        }
        if(over == false) {
            logger.error({
                message: 'task is not on list',
                action: req.method,
                path: req.path,
                body: req.body,
                time: new Date()
            })
            next()
        res.send(`${taskName} is not on the list`)
        }
}
})
//----------------------------------------------------------------------------------------------
app.listen(3000)
console.log("Server is running on port 3000")