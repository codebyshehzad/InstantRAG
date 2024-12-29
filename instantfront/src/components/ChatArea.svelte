<!-- src/components/ChatArea.svelte -->
<script>
    import { onMount } from 'svelte';

    // Store for chat messages
    let messages = [];
    let chatContainer;

    // Function to add new message
    export const addMessage = (message, isUser = true) => {
        messages = [...messages, { 
            id: Date.now(),
            sender: isUser ? "User" : "AI",
            text: message,
            timestamp: new Date().toLocaleTimeString()
        }];
        
        // Scroll to bottom on new message
        setTimeout(() => {
            if (chatContainer) {
                chatContainer.scrollTop = chatContainer.scrollHeight;
            }
        }, 100);
    };

    onMount(() => {
        // Initial welcome message
        if (messages.length === 0) {
            addMessage("Hello! I'm here to help you analyze your documents. Feel free to upload a document or ask me questions.", false);
        }
    });
</script>

<div class="chat-area" bind:this={chatContainer}>
    {#each messages as message (message.id)}
        <div class={`message ${message.sender === "User" ? "user" : "ai"}`}>
            <div class="message-content">
                {message.text}
            </div>
            <div class="message-timestamp">
                {message.timestamp}
            </div>
        </div>
    {/each}
</div>
<style>
  .chat-area {
    flex: 1;
    padding: 20px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    background: #1e1e2f;
    color:white;
  }
</style>
