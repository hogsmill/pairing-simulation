<template>
  <nav class="navbar navbar-expand-lg navbar-light mb-4">
    <a class="navbar-brand" href="https://agilesimulations.co.uk">
      <img src="/lego.png" class="ml-4" height="38px">
    </a>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon" />
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <h1>Pairing Simulation</h1>
      <ul class="navbar-nav ml-auto">
        <li class="nav-item" :class="{ active: !showAbout }">
          <a class="nav-link pointer" @click="updateShowAbout(false)">Simulation</a>
        </li>
        <li class="nav-item" :class="{ active: showAbout }">
          <a class="nav-link pointer" @click="updateShowAbout(true)">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link pointer" @click="show()">Feedback</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import mailFuns from '../lib/mail.js'

export default {
  computed: {
    thisGame() {
      return this.$store.getters.thisGame
    },
    showAbout() {
      return this.$store.getters.getShowAbout
    },
  },
  created() {
    if (location.search == '?host') {
      this.$store.dispatch('updateHost', true)
    }
  },
  methods: {
    updateShowAbout(payload) {
      this.$store.dispatch('updateShowAbout', payload)
    },
    show () {
      this.$store.dispatch('showModal', 'feedback')
    }
  }
}
</script>

<style>
  h1 {
    letter-spacing: initial;
    margin-left: 6px;
    font-weight: bold;
    text-shadow: 2px 2px 3px #444;
    font-size: xx-large;
    line-height: 1;
  }
  .feedback {
    letter-spacing: 0;
    color: #212529;
  }

  p.feedback-form {
    margin-bottom: 12px;
  }

  .feedback-form {
    width: 80%;
    margin: 0 auto;
  }
</style>
