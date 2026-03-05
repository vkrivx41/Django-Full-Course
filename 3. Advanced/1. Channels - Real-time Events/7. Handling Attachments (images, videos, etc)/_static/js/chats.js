
const states = {
    room: null,
    sender: null,
    typing: false
}

const IMAGE = "image"
const VIDEO = "video"
const AUDIO = "audio"
const DOCUMENT = "document"

const media_types = {
    "image/jpeg": IMAGE,
    "image/png": IMAGE,
    "image/gif": IMAGE,
    "image/svg+xml": IMAGE,
    "image/webp": IMAGE,
    "image/avif": IMAGE,

    "video/mp4": VIDEO,
    "video/webm": VIDEO,
    "video/ogg": VIDEO,
    "video/mkv": VIDEO,

    "audio/mpeg": AUDIO,
    "audio/wav": AUDIO,
    "audio/acc": AUDIO,
    "audio/mp3": AUDIO,
    "audio/ogg": AUDIO,
    "audio/flac": AUDIO,

    "application/pdf": DOCUMENT,
    "application/msword": DOCUMENT,
    "application/vnd.ms-excel": DOCUMENT,
    "text/plain": DOCUMENT,
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

    data.forEach(({ online, sender, sender_id, receiver_id, room_id, room_name, unreads }) => {
        const isActiveClass = online ? "active" : ""
        template += `
        <div class="chat-content" id=${room_name} room=${room_name} room_id=${room_id} sender=${sender}  sender_id=${sender_id} receiver_id=${receiver_id}>
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
            let message = data.content
            let sender = data.sender
            let room = data.room
            let attachment_url = data.attachment_url
            let media_type = media_types[data.attachment_type]

            const chats = document.querySelector(".chats")
            const targetChat = chats.querySelector(`#${room}`)

            let roomIsActive = targetChat.getAttribute("class").includes("active")

            if (roomIsActive) {
                states.room = targetChat.getAttribute("room")
                const messages_div = document.querySelector(".previous-messages")

                const message_class = states.sender == sender ? "right" : "left"
                let message_template = ""

                if (attachment_url) {
                    message_template = getTemplateText(media_type, message_class, attachment_url, message)
                } else {
                    message_template = `
                        <div class="message">
                            <div class="message-body ${message_class}">
                                ${message}
                            </div>
                        </div>`
                }

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
    const attachment = form.querySelector("#attachment")

    attachment.addEventListener("change", (e) => {
        const attachmentLabel = document.querySelector("#attachment-label")
        setActiveClass(attachmentLabel, "active")
    })

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

    form.addEventListener('submit', async (e) => {
        e.preventDefault()

        performMessageSending(e, socket)

        form.reset()
    })
}

async function performMessageSending(e, socket) {
    let fileInput = document.querySelector('input[type="file"]')
    const message = e.target.message.value

    const csrfToken = getCookie('csrftoken')

    const attachment = fileInput?.files[0]
    let attachment_url = null
    let attachment_type = null

    if (attachment) {
        const presignedData = await getPresignedData(attachment)

        if (presignedData.error) {
            alert(presignedData.error)
            return
        }
        const uploaded = await uploadAttachment(attachment, presignedData)

        if (uploaded) {
            attachment_url = presignedData.fields.key
            attachment_type = presignedData.fields["Content-Type"]
        }
    }

    const messageData = await createMessage(message, attachment_url, attachment_type, csrfToken)

    messageData.sender = states.sender
    messageData.room = states.room

    socket.send(JSON.stringify({
        'type': 'message',
        ...messageData
    }))
}


async function getPresignedData({ name, size, type }) {
    const formData = {
        name,
        size,
        type
    }

    const csrfToken = getCookie("csrftoken")

    const request = await fetch(
        "/upload-attachment/",
        {
            method: "POST",
            body: JSON.stringify(formData),
            headers: {
                "X-CsrfToken": csrfToken,
                "Content-Type": "application/json"
            }
        }
    )
    return await request.json()
}

async function uploadAttachment(file, presignedData) {
    return new Promise((resolve, reject) => {
        xhr = new XMLHttpRequest()
        const progressBar = document.querySelector(".progress-bar")
        const progressBarComplete = progressBar.querySelector(".complete-bar")
        setActiveClass(progressBar, "active")

        xhr.open("POST", presignedData.upload_url, true)

        xhr.upload.onprogress = function (event) {
            if (event.lengthComputable) {
                const percent = Math.round((event.loaded / event.total) * 100)
                console.log(`Uploaded: ${percent}%`)
                progressBarComplete.style.width = `${percent}%`
            }
        }

        xhr.onload = function () {
            if (xhr.status == 201 || xhr.status == 204) {
                progressBar.removeAttribute("class")
                progressBar.setAttribute("class", "progress-bar")

                const attachmentLabel = document.querySelector("#attachment-label")
                attachmentLabel.removeAttribute("class")
                return resolve(true)
            } else {
                console.error("Upload Failed", xhr.responseText)
                return reject(false)
            }
        }

        xhr.onerror = function () {
            console.error("An error occured while uploading")
            return reject(false)
        }

        const newFormData = new FormData()

        // include all fields except the Content-Type
        Object.entries(presignedData.fields).forEach(([key, value]) => {
            if (key != "Content-Type") {
                newFormData.append(key, value)
            }
        })
        // append the file after the key field
        newFormData.append("file", file)

        xhr.send(newFormData)
    })
}

async function createMessage(message, attachment_url, attachment_type, csrfToken) {
    const request = await fetch(
        "/create-message/",
        {
            method: "POST",
            body: JSON.stringify({
                "attachment": attachment_url,
                "attachment_type": attachment_type,
                "content": message,
                "room": states.room_id
            }),
            headers: {
                'Content-Type': "application/json",
                "X-CsrfToken": csrfToken
            }
        }
    )
    return await request.json()
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
    const room_id = clickedChat.getAttribute("room_id")
    const sender_id = clickedChat.getAttribute("sender_id")

    states.room = room
    states.room_id = room_id

    setActiveChat(clickedChat)
    readMessages(clickedChat)

    const messages_div = document.querySelector(".previous-messages")

    const response = await fetch(`/room-messages/?room=${room}`)
    const data = await response.json()

    const previous_messages = data

    let text = ''

    previous_messages.forEach(({ sender, content, attachment_url, attachment_type }) => {
        const message_class = sender == sender_id ? "right" : "left"
        const media_type = media_types[attachment_type]


        if (attachment_url) {
            text += getTemplateText(media_type, message_class, attachment_url, content)
        } else {
            text += `
                <div class="message">
                    <div class="message-body ${message_class}">
                        ${content}
                    </div>
                </div>`
        }

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


function getTemplateText(media_type, message_class, attachment_url, content) {
    switch (media_type) {
        case IMAGE:
            return `
                <div class="message">
                    <div class="message-body ${message_class}">
                        <img src=${attachment_url} alt="Not found">
                        ${content}
                    </div>
                </div>`
            break;
        case VIDEO:
            return `
                <div class="message">
                    <div class="message-body ${message_class}">
                        <video src=${attachment_url} controls></video>
                        ${content}
                    </div>
                </div>`
        case AUDIO:
            return `
                <div class="message">
                    <div class="message-body ${message_class}">
                        <audio src=${attachment_url} controls></audio>
                        ${content}
                    </div>
                </div>`
        case DOCUMENT:
            return `
                <div class="message">
                    <div class="message-body ${message_class}">
                        DOCUMENT 📄
                        ${content}
                    </div>
                </div>`
        default:
            return `
            <div class="message">
                <div class="message-body ${message_class}">
                    <div><b>Content Can't be Displayed</b></div>
                    ${content}
                </div>
            </div>`
    }
}