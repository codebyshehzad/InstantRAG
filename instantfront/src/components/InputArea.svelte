<!-- src/components/InputArea.svelte -->
<script>
    import { apiService } from '../services/api.js';
    
    // Import the addMessage function from parent
    export let addMessage;
    
    let message = '';
    let isLoading = false;
    let errorMessage = '';
    
    // Handle sending text messages
    async function sendMessage() {
        if (!message.trim() || isLoading) return;
        
        try {
            isLoading = true;
            errorMessage = '';
            
            // Add user message to chat
            addMessage(message, true);
            const userMessage = message;
            message = '';
            
            // Get AI response
            const response = await apiService.sendQuery(userMessage);
            addMessage(response, false);
            
        } catch (error) {
            errorMessage = error.message;
            addMessage(`Error: ${error.message}`, false);
        } finally {
            isLoading = false;
        }
    }
    
    // Handle file uploads
    async function handleFileUpload(event) {
        const file = event.target.files[0];
        if (!file) return;
        
        try {
            isLoading = true;
            errorMessage = '';
            
            addMessage(`Uploading file: ${file.name}...`, true);
            
            const result = await apiService.uploadDocument(file);
            addMessage(`File uploaded successfully! ${result.message}`, false);
            
            // Clear the file input
            event.target.value = '';
            
        } catch (error) {
            errorMessage = error.message;
            addMessage(`Error uploading file: ${error.message}`, false);
        } finally {
            isLoading = false;
        }
    }
</script>

<div class="input-container">
    {#if errorMessage}
        <div class="error-message">
            {errorMessage}
        </div>
    {/if}
    
    <div class="input-area">
        <input
            type="text"
            bind:value={message}
            placeholder={isLoading ? "Processing..." : "Type a message..."}
            disabled={isLoading}
            on:keydown={(e) => e.key === 'Enter' && sendMessage()}
        />
        
        <button 
            on:click={sendMessage} 
            disabled={isLoading}
            class:loading={isLoading}
            title="Send"
        >
            <i class="send-icon">➤</i>
        </button>
        
        <label class="attachment" class:loading={isLoading}>
            <input 
                type="file" 
                accept=".txt"
                on:change={handleFileUpload}
                disabled={isLoading}
                hidden 
            />
            <i class="attachment-icon">📎</i>
        </label>
    </div>
</div>

<style>
    .input-container {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }

    .input-area {
        display: flex;
        align-items: center;
        padding: 15px;
        background: #282840;
        border-top: 1px solid #3a3a5c;
    }

    .error-message {
        color: #ff6b6b;
        padding: 8px;
        background: rgba(255, 107, 107, 0.1);
        border-radius: 4px;
        font-size: 0.9rem;
    }

    input {
        flex: 1;
        padding: 15px;
        border: none;
        border-radius: 5px;
        font-size: 1rem;
        color: #fff;
        background: #3a3a5c;
    }

    input:disabled {
        opacity: 0.7;
        cursor: not-allowed;
    }

    input::placeholder {
        color: #aaa;
    }

    button {
        background: none;
        border: none;
        cursor: pointer;
        margin-left: 10px;
        font-size: 1.5rem;
        color: #4caf50;
        transition: color 0.3s;
        opacity: 1;
    }

    button:disabled {
        cursor: not-allowed;
        opacity: 0.5;
    }

    button.loading {
        animation: pulse 1.5s infinite;
    }

    .attachment {
        margin-left: 10px;
        cursor: pointer;
        opacity: 1;
    }

    .attachment.loading {
        opacity: 0.5;
        cursor: not-allowed;
    }

    .attachment-icon {
        font-size: 1.5rem;
        color: #4caf50;
    }

    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
</style>