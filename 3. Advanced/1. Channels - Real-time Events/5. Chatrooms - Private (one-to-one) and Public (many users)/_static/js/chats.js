
document.addEventListener('DOMContentLoaded', () => {
    startApp()
})


function startApp(){
    scrollChatMessages()
}

function scrollChatMessages(){
    const previousMessages = document.querySelector(".previous-messages")
    previousMessages.scrollTop = previousMessages.scrollHeight
}


function setActiveClass(element, newClass){
    let currentClass = element.getAttribute("class")
    element.setAttribute("class", `${currentClass} ${newClass}`)
}

function setActiveChat(clickedChat){
    const defaultMessage = document.querySelector(".message-content-default")
    const previousMessages = document.querySelector(".previous-messages")
    const messageInput = document.querySelector(".message-input")
    const chats = document.querySelectorAll(".chat-content")

    for (let index = 0; index < chats.length; index++) {
        const element = chats[index];
        element.setAttribute("class", "chat-content")
    }
    
    setActiveClass(clickedChat, 'active')
    setActiveClass(defaultMessage, 'close')
    setActiveClass(previousMessages, 'open')
    setActiveClass(messageInput, 'open')
}


const states = {
}


function createRoom(event){
    const clickedChat = event.target
    const room = clickedChat.getAttribute("room")
    const sender = clickedChat.getAttribute("sender")
    const sender_id = clickedChat.getAttribute("sender_id")

    states.room = room

    setActiveChat(clickedChat)

    let url = `ws://${window.location.host}/ws/socket/?room=${room}`

    const chatSocket = new WebSocket(url)

    const messages_div = document.querySelector(".previous-messages")

    chatSocket.onmessage = (e) => {
        const data = JSON.parse(e.data)
        
        if (data.type == 'connections.established'){
            const previous_messages = JSON.parse(data.messages)
            let text = ''

            previous_messages.forEach(({fields}) => {
                const message_class = fields.sender == sender_id ? "right": "left"

                text += `<div class="message">
                    <div class="message-body ${message_class}">${fields.content}</div>
                </div>`
            });
            messages_div.innerHTML = text
            scrollChatMessages()
        }

        if (data.type == 'chat'){
            const message_class = data.sender == sender ? "right": "left"
            let message_template = `<div class="message">
                    <div class="message-body ${message_class}">${data.message}</div>
                </div>`

            messages_div.insertAdjacentHTML('beforeend', message_template)
            scrollChatMessages()
        }
    }

    const form = document.getElementById("message-form")

    form.addEventListener('submit', (e) => {
        e.preventDefault()

        message = e.target.message.value

        if (message === null || message === "") {
            return
        };

        chatSocket.send(JSON.stringify({
            'message': message,
            'room': states.room,
            'sender': sender,
        }))

        form.reset()
    })
}
