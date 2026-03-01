
const states = {
    room: null,
    sender: null,
    typing: false
}

document.addEventListener('DOMContentLoaded', () => {
    startApp()
})


function startApp() {
    getOnlineData()
    setOnlineIndicators()

    document.addEventListener("click", (e) => {
        let userField = e.target
        if (["online-indicator", "user-name"].includes(userField.getAttribute("class"))) {
            createRoom(userField.parentElement)
        } else if (userField.getAttribute == "chat-content") {
            createRoom(userField)
        }
    })
}


function scrollChatMessages() {
    const previousMessages = document.querySelector(".previous-messages")
    previousMessages.scrollTop = previousMessages.scrollHeight
}

async function getOnlineData() {
    const response = await fetch("/home-data/")
    let data = await response.json()
    const chats = document.querySelector(".chats")
    let template = ''

    states.sender = data.sender
    data = data.data

    data.forEach(({ online, sender, sender_id, receiver_id, room_name, unreads }) => {
        const isActiveClass = online ? "active" : ""
        template += `
        <div class="chat-content" id=${room_name} room=${room_name} sender=${sender}  sender_id=${sender_id} receiver_id=${receiver_id}>
            <div class="online-indicator ${isActiveClass}"></div>
            <div class="user-name">
                ${receiver_id}
            </div>
            ${(unreads > 0) ? `<div class="unread-messages">${unreads}</div>` : ``}
        </div>`
    });

    chats.innerHTML = template
}


function setOnlineIndicators() {
    const url = `ws://${window.location.host}/presence/`
    const socket = new WebSocket(url)

    setHeartBeatInterval(socket)

    socket.onmessage = (e) => {
        const data = JSON.parse(e.data)
        const chats = document.querySelectorAll(".chat-content")

        if (data.type == "indicator") {
            for (let index = 0; index < chats.length; index++) {
                const element = chats[index];
                let receiver_id = element.getAttribute("receiver_id")

                if (receiver_id == data.user_id) {
                    const onlineIndicator = element.querySelector(".online-indicator")

                    if (data.event == "online") {
                        setActiveClass(onlineIndicator, "active")
                    } else if (data.event == "offline") {
                        let currentClass = onlineIndicator.getAttribute("class").split(" ")[0]
                        onlineIndicator.setAttribute("class", currentClass + " in-active")
                    }
                }
            }
        }
        else if (data.type == "typing") {
            let room = data.room
            let sender = data.sender

            states.typing = true

            const chats = document.querySelector(".chats")
            const targetChat = chats.querySelector(`#${room}`)

            let roomIsActive = targetChat.getAttribute("class").includes("active")

            if (roomIsActive) {
                states.room = targetChat.getAttribute("room")
                const messages_div = document.querySelector(".previous-messages")

                const message_class = "left"
                let message_template = `<div class="message">
                        <div class="message-body ${message_class}">Typing...</div>
                    </div>`

                messages_div.insertAdjacentHTML('beforeend', message_template)
                setTimeout(() => {
                    messages_div.removeChild(messages_div.lastChild)
                    states.typing = false
                }, 1000)

                scrollChatMessages()
            }
        }
        else if (data.type == "chat") {
            let message = data.message
            let sender = data.sender
            let room = data.room

            // get the room the chat is to
            // if the room is not open, then update it's unread-messages count
            // if the room is open, then, write the message, scroll to the bottom, and mark the messages as read

            const chats = document.querySelector(".chats")
            const targetChat = chats.querySelector(`#${room}`)

            let roomIsActive = targetChat.getAttribute("class").includes("active")

            if (roomIsActive) {
                states.room = targetChat.getAttribute("room")
                const messages_div = document.querySelector(".previous-messages")

                const message_class = states.sender == sender ? "right" : "left"
                let message_template = `<div class="message">
                        <div class="message-body ${message_class}">${message}</div>
                    </div>`

                if (states.typing) {
                    setTimeout(() => {
                        messages_div.insertAdjacentHTML('beforeend', message_template)
                    }, 1000);
                } else {
                    messages_div.insertAdjacentHTML('beforeend', message_template)
                }

                scrollChatMessages()
                readMessages(targetChat)

            } else if (!roomIsActive) {
                let unreadMessagesElement = targetChat.querySelector(".unread-messages")
                if (!unreadMessagesElement) {
                    unreadMessagesElement = document.createElement("div")
                    unreadMessagesElement.setAttribute("class", "unread-messages")

                    targetChat.appendChild(unreadMessagesElement)
                    unreadMessagesElement.innerText = 0
                }
                let unreadMessages = parseInt(unreadMessagesElement.innerText.trim())
                unreadMessages += 1

                unreadMessagesElement.style.display = "block"
                unreadMessagesElement.innerText = unreadMessages
            }
        }
    }

    /**
    - Set an onchange event-listener on the message input
    - Use debounce to send the signal after a timeout of 5secs
    - receive the signal
    - create a timeout of 3 secs and send the signal inside that time
    - if there is an on going timeout then clear it
     */

    const form = document.getElementById("message-form")
    const messageInput = form.querySelector("#message")

    let typingTimer = null

    messageInput.addEventListener("input", (e) => {
        if (typingTimer) {
            clearTimeout(typingTimer)
        }

        typingTimer = setTimeout(() => {
            socket.send(JSON.stringify({
                'type': 'typing',
                'room': states.room,
                'sender': states.sender
            }))
        }, 500);
    })

    form.addEventListener('submit', (e) => {
        e.preventDefault()

        message = e.target.message.value

        if (message === null || message === "") {
            return
        };

        socket.send(JSON.stringify({
            'type': 'message',
            'message': message,
            'room': states.room,
            'sender': states.sender
        }))

        form.reset()
    })
}


function setHeartBeatInterval(socket) {
    setInterval(() => {
        socket.send(
            JSON.stringify({
                type: "heartbeat"
            })
        )
    }, 15000);
}

function setActiveClass(element, newClass) {
    let currentClass = element.getAttribute("class")
    element.setAttribute("class", `${currentClass} ${newClass}`)
}

function setActiveChat(clickedChat) {
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


async function createRoom(clickedChat) {
    const room = clickedChat.getAttribute("room")
    const sender_id = clickedChat.getAttribute("sender_id")

    states.room = room

    setActiveChat(clickedChat)
    readMessages(clickedChat)

    const messages_div = document.querySelector(".previous-messages")

    const response = await fetch(`/room-messages/?room=${room}`)
    const data = await response.json()

    const previous_messages = data

    let text = ''

    previous_messages.forEach(({ sender, content }) => {
        const message_class = sender == sender_id ? "right" : "left"

        text += `<div class="message">
            <div class="message-body ${message_class}">${content}</div>
        </div>`
    });
    messages_div.innerHTML = text
    scrollChatMessages()

    messages_div.addEventListener('scroll', async (e) => {
        if (messages_div.scrollTop === 0) {
            console.log("you've reached the top")
        }
    })
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


async function readMessages(clickedChat) {
    const csrfToken = getCookie('csrftoken')

    const response = await fetch(
        "/read-messages/",
        {
            method: "POST",
            body: JSON.stringify({ room: states.room }),
            headers: {
                "Content-Type": "application/json",
                "X-CsrfToken": csrfToken
            },
            mode: "same-origin"
        }
    )

    const data = await response.json()
    const unreadMessagesElement = clickedChat.querySelector(".unread-messages")
    if (!unreadMessagesElement) return // if no unread messages

    unreadMessagesElement.innerText = 0
    unreadMessagesElement.style.display = 'none'
}
