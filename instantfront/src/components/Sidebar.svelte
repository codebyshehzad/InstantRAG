<script>
  let menuItems = ["Dashboard", "Messages", "Settings", "Profile"];
</script>

<div class="sidebar">
  <div class="logo">Home</div>
  <ul class="menu">
    {#each menuItems as item}
      <li class="menu-item">{item}</li>
    {/each}
  </ul>
</div>
<style>
  .sidebar {
    width: 200px;
    flex-shrink: 0;
    background: #282840;
    color:white;
    display: flex;
    flex-direction: column;
    padding: 20px;
  }

  @media (max-width: 768px) {
    .sidebar {
      width: 100%;
      flex-direction: row;
      overflow-x: auto;
    }
  }
</style>
