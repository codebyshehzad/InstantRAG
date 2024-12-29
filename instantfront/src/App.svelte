<script>
  import Sidebar from './components/Sidebar.svelte';
  import Header from './components/Header.svelte';
  import ChatArea from './components/ChatArea.svelte';
  import InputArea from './components/InputArea.svelte';

  let chatAreaComponent;
</script>

<div class="app-container">
  <Sidebar />
  <div class="main-content">
    <Header />
    <div class="chat-section">
      <ChatArea bind:this={chatAreaComponent} />
      <InputArea addMessage={chatAreaComponent?.addMessage} />
    </div>
  </div>
</div>

<style>
  .app-container {
    display: flex;
    height: 100vh;
    overflow: hidden;
  }

  .main-content {
    display: flex;
    flex-direction: column;
    flex: 1;
    overflow: hidden;
    background: #1e1e2f;
  }

  .chat-section {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow-y: hidden;
  }
</style>
