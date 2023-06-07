<template>
  <nav class="navbar navbar-expand-sm navbar-light bg-light">
    <div class="container">
      <img src="/public/VUE_Django_2.png" class="logo rounded float-start pe-5" alt="VUE_Django">
      <a class="navbar-brand" href="#"> Flash Card</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" href="#">Card Sets</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Study</a>
          </li>
        </ul>
        <img src="../../public/Under_Construction_1.png" class="logo rounded float-end ps-5" alt="Under_Construction">
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "AppHeader",
};
</script>

<style scoped>
.logo {
  height: 5rem
}
</style>