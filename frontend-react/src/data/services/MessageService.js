
let mockMessages = [
    { id: 1, message : "Mock Message 1" } ,
];

class MessageService {
    
    static async getMessages() {
        return mockMessages; 
    }

    static async addMessage(newMessage) {
        mockMessages.push(newMessage);
    }

    static async updateMessage(updateMessage) {
        // updateMessage
    }

    static async deleteMessage(messageId) {
        // deleteMesage
    }

}

export default MessageService; 