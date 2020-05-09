<template>
  <div class="about">
    <h2>The Pairing Simulation</h2>
    <p>An app to explore how knowledge sharing through pairing influences speed and
       quality of software development.</p>

    <h3>Strategies</h3>

    <p>There a number strategies when pairing; this simulation aims to explore the
       differences and work out which worst best in which circumstances.</p>

    <ol>
      <li><strong>No Pairing</strong> this is the control group. We hope to show that this is a bad strategy :-)</li>
      <li><strong>Best Pairing</strong> put the 2 team members with the most relevant knowledge on every task</li>
      <li><strong>Best Sharing</strong> put the most expert, and the least expert on every task</li>
      <li><strong>Worst Pairing</strong> put the 2 least expert team members on each task</li>
      <li><strong>Random</strong> randomly assign team members to each task</li>
    </ol>

    <p>Additionally, every pairing strategy can <strong>swap</strong> one of the pair - or not - after
       each cycle to further spread the knowledge. As with pairing, there are a number of
       strategies:</p>

    <ol>
      <li><strong>Swap Weakest</strong> change the pair with the least expertise for the task</li>
      <li><strong>Swap Strongest</strong> change the pair with most expertise</li>
      <li><strong>Random</strong> randomly swap somebody off the task</li>
    </ol>

    <p>(<em>Note: Swapping not yet implemented</em>)</p>

    <h3>How it works</h3>

    <p>We have a simple Kanban board - To Do, Doing, Done.</p>

    <p>We have a set of cards that we want to move from To Do to Done. Each card requires
      a particular skill, and an amount of that skill to complete it, e.g. JavaScript: 100
      or SQL: 50

    <p>We have a team - a set of members who each have a set of skills, e.g. JavaScript: 10
       and CSS: 20. Every time a team member works on a card, they increase their level of the
       skills on the card, up to a maximum "expert" level. As an example, working on a
       JavaScript card could raise JavaScript: 10 to JavaScript: 20</p>

    <p>Members learn different amounts depending who they are pairing with:</p>
    <ul>
      <li>If they pair with somebody who has the skill required for the card, they learn (e.g.) 10% of that experts knowledge</li>
      <li>If no-one on the card has the required knowledge, they learn a s small default amount, e.g. 1</li>
    </ul>

    <p>Team members use their skills to work on a card. They complete the amount of work
       on the card of the skill they have. As an example, if the card had JavaScript: 50,
       and the member had JavaScript: 20, after they had worked on the card, there would
       be 30 JavaScript left. (<em>There is a maximum amount of work that can be done, though...</em>)</p>

    <p>Work is done in cycles:</p>
    <ol>
      <li>Members are assigned to as many cards as possible, given the pairing strategy,
          e.g. 2 on each if pairing. Once  card has members assigned, it is moved to Doing</li>
      <li>The amount of work for the cycle is calculated. If the card is complete, it is moved to complete</li>
    </ol>
  </div>
</template>

<style>
  .about { padding: 12px; }
  h3, p, ol, ul, li { text-align: left; }
</style>
