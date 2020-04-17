# pairing-simulation

An app to explore how knowledge sharing through pairing influences speed and
quality of software development.

## Strategies

1. **No Pairing** this is the control group. We hope to show that this is a bad strategy :-)
1. **Best Pairing** put the 2 team members with the best knowledge on every task
1. **Best Sharing** put the most expert, and the least expert on every task
1. **Worst Pairing** put the 2 least expert team members on each task
1. **Random** randomly assign team members to each task

Additionally, every pairing strategy can **swap** one of the pair - or not - after
each cycle to further spread the knowledge. As with pairing, there are a number of
strategies:

1. **Swap Weakest** change the pair with the least expertise for the task
1. **Swap Strongest** change the pair with most expertise
1. **Random** randomly swap somebody off the task

(Swapping not yet implemented)

## How it works

We have a simple Kanban board - To Do, Doing, Done.

We have a set of cards that we want to move from To Do to Done. Each card has a
set of skills needed, and a level of those skills, e.g. JavaScript: 100 or SQL: 50

We have a team - a set of members who each have a set of skills, e.g. JavaScript: 10
and CSS: 20. Every time a team member works on a card, they increase their level of the
skills on the card, up to a maximum "expert" level. As an example, working on a
JavaScript card would raise JavaScript: 10 to JavaScript: 20

Team members use their skills to work on a card. They complete the amount of work
on the card of the skill they have. As an example, if the card had JavaScript: 50,
and the member had JavaScript: 20, after they had worked on the card, there would
be 30 JavaScript left.

Work is done in cycles:
1. Members are assigned to as many cards as possible, e.g. 2 on each if pairing. Once  card has members assigned, it is moved to Doing
1. 
